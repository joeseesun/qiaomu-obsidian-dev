#!/usr/bin/env python3
"""Read-only local Obsidian release audit; does not establish marketplace approval."""
import argparse
import hashlib
import json
import re
from pathlib import Path


def audit(root, tag=None, budget=5_000_000):
    root = Path(root).resolve()
    failures, assets = [], {}
    def read_json(name, required=True):
        path = root / name
        if not path.exists() and not required:
            return None
        try:
            value = json.loads(path.read_text())
            if not isinstance(value, dict):
                raise ValueError('expected object')
            return value
        except (OSError, ValueError) as error:
            failures.append(f'{name}: {error.__class__.__name__}')
            return {}
    manifest = read_json('manifest.json')
    version = manifest.get('version')
    for field in ('id', 'name', 'version', 'minAppVersion', 'description', 'author'):
        if not isinstance(manifest.get(field), str) or not manifest[field].strip():
            failures.append(f'manifest missing or invalid {field}')
    if not isinstance(manifest.get('isDesktopOnly'), bool):
        failures.append('manifest isDesktopOnly must be boolean')
    if not re.fullmatch(r'\d+\.\d+\.\d+', str(version)):
        failures.append('manifest version must be x.y.z')
    if tag is not None and tag != version:
        failures.append('tag must equal manifest version exactly')
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', str(manifest.get('id', ''))) or 'obsidian' in str(manifest.get('id', '')).lower():
        failures.append('invalid plugin id')
    package = read_json('package.json', False)
    if package is not None and package.get('version') != version:
        failures.append('package version differs from manifest')
    versions = read_json('versions.json', False)
    if versions is not None and (not isinstance(version, str) or versions.get(version) != manifest.get('minAppVersion')):
        failures.append('versions.json does not map this version to minAppVersion')
    for name in ('main.js', 'manifest.json', 'styles.css'):
        path = root / name
        if name == 'styles.css' and not path.exists():
            continue
        try:
            data = path.read_bytes()
            assets[name] = {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}
            if not data:
                failures.append(f'{name} is empty')
            if len(data) > budget:
                failures.append(f'{name} exceeds configured {budget}-byte budget')
        except OSError:
            failures.append(f'{name} missing or unreadable')
    return {'ok': not failures, 'version': version, 'assets': assets, 'failures': failures,
            'scope': 'local artifacts only; no review, runtime or permission certification'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', type=Path)
    parser.add_argument('--tag')
    parser.add_argument('--max-asset-bytes', type=int, default=5_000_000)
    args = parser.parse_args()
    if args.max_asset_bytes < 1:
        parser.error('--max-asset-bytes must be positive')
    result = audit(args.root, args.tag, args.max_asset_bytes)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result['ok'] else 1)


if __name__ == '__main__':
    main()
