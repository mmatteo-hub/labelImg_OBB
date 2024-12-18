# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['labelImg.py'],
    pathex=['./libs', './'],
    binaries=[],
    datas=[],
    hiddenimports=['lxml', 'PyQt5', 'xml', 'xml.etree', 'xml.etree.ElementTree', 'lxml.etree'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='labelImg',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
