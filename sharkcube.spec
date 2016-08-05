# -*- mode: python -*-

block_cipher = None

data = [
    ('./templates/', './templates'),
    ('pycoil.py', '.'),
    ('./static/', './static')
    ]

a = Analysis(['sharkcube.py'],
             pathex=['/Users/edelsonc/Documents/Documents/School/NCF/SharkCube_app'],
             binaries=None,
             datas=data,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='sharkcube',
          debug=False,
          strip=False,
          upx=True,
          console=False )
app = BUNDLE(exe,
             name='sharkcube.app',
             icon='./SharkCube.icns',
             bundle_identifier=None)
