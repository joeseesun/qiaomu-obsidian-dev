import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('audit', Path(__file__).resolve().parents[1] / 'scripts/audit_release.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class ReleaseAuditTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.manifest = dict(id='reading-tool', name='Reader', version='1.2.3', minAppVersion='1.0.0', description='Read', author='Author', isDesktopOnly=False)
        self.write('manifest.json', self.manifest)
        (self.root/'main.js').write_text('console.log("fixture")')
    def write(self, name, value):
        (self.root/name).write_text(json.dumps(value))
    def test_optional_css_passes(self):
        result=module.audit(self.root, '1.2.3'); self.assertTrue(result['ok']); self.assertEqual(len(result['assets']['main.js']['sha256']),64)
    def test_v_prefix_fails(self):
        self.assertFalse(module.audit(self.root,'v1.2.3')['ok'])
    def test_missing_js(self):
        (self.root/'main.js').unlink(); self.assertFalse(module.audit(self.root)['ok'])
    def test_empty_js(self):
        (self.root/'main.js').write_bytes(b''); self.assertFalse(module.audit(self.root)['ok'])
    def test_package_mismatch(self):
        self.write('package.json',dict(version='1.2.2')); self.assertFalse(module.audit(self.root)['ok'])
    def test_invalid_json(self):
        (self.root/'manifest.json').write_text('{'); self.assertFalse(module.audit(self.root)['ok'])
    def test_versions_mismatch(self):
        self.write('versions.json',{'1.2.3':'2.0.0'}); self.assertFalse(module.audit(self.root)['ok'])
    def test_bytes_not_characters(self):
        (self.root/'main.js').write_text('乔'*200); self.assertFalse(module.audit(self.root,budget=500)['ok'])
    def test_read_only(self):
        before={p.name:p.read_bytes() for p in self.root.iterdir()}; module.audit(self.root); self.assertEqual(before,{p.name:p.read_bytes() for p in self.root.iterdir()})
    def test_invalid_id(self):
        self.manifest['id']='obsidian-thing'; self.write('manifest.json',self.manifest); self.assertFalse(module.audit(self.root)['ok'])

    def test_non_string_version_with_mapping_returns_failure(self):
        self.write('versions.json', {'1.2.3': '1.0.0'})
        for version in ([], {}, None, 123):
            with self.subTest(version=version):
                self.manifest['version'] = version
                self.write('manifest.json', self.manifest)
                result = module.audit(self.root)
                self.assertFalse(result['ok'])
                self.assertIn('manifest missing or invalid version', result['failures'])
