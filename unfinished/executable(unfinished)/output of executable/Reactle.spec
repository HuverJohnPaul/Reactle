# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['Reactle\\executable\\executable_creator_script.py'],
    pathex=[],
    binaries=[],
    datas=[('Reactle/periodictable.csv', '.'), ('Reactle/main.py', '.'), ('Reactle/database/*', '.')],
    hiddenimports=[],
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
    name='Reactle',
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
    icon=['Reactle\\Visualization (work in progress)\\images\\reactle-icon.ico'],
)
