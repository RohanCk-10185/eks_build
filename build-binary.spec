# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['/home/ubuntu/EKS-dashboard_prod/app.py'],
    pathex=[],
    binaries=[],
    datas=[('/home/ubuntu/EKS-dashboard_prod/static', 'static'), ('/home/ubuntu/EKS-dashboard_prod/templates', 'templates'), ('/home/ubuntu/EKS-dashboard_prod/saml_config', 'saml_config')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='build-binary',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
