# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Main.py','feature_1.py','feature_3.py','data_smooth_new_try_1_4_3.py','feature_4.py','feature_4_all.py','math_test.py','pixelbetweenpoints.py','data_smooth.py'],
             pathex=['C:\\Users\\40520\\PycharmProjects\\cell_detection_1.0.0\\feature_test_1.0.1'],
             binaries=[],
             datas=[('C:\\Users\\40520\\PycharmProjects\\cell_detection_1.0.0\\feature_test_1.0.1\\bin','bin'),('C:\\Users\\40520\\PycharmProjects\\cell_detection_1.0.0\\feature_test_1.0.1\\result','result'),('C:\\Users\\40520\\PycharmProjects\\cell_detection_1.0.0\\feature_test_1.0.1\\output_single','output_single'),('C:\\Users\\40520\\PycharmProjects\\cell_detection_1.0.0\\feature_test_1.0.1\\paper_test','paper_test'),('C:\\Users\\40520\\PycharmProjects\\cell_detection_1.0.0\\feature_test_1.0.1\\temp_file','temp_file')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Main')
