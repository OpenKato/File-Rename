# -*- coding: utf-8 -*-
import glob, os, time
files = glob.glob("*.jpg")
for i, old_name in enumerate(files):
    t = os.path.getmtime(old_name)
    ts = time.strftime("%Y%m%d", time.localtime(t))
    new_name = "{0:s}-{1:03d}.jpg".format(ts, i + 1)
    os.rename(old_name, new_name)
    print(old_name + "9" + new_name)

#os.path.getctime()	ファイルの作成日時
#os.path.getmtime()	ファイルの更新日時
#os.path.getatime()	ファイルへのアクセス日時
#os.path.getsize()	ファイルのサイズ
