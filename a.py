import os

f = open("filelists/ljs_audio_text_train_filelist.txt", 'rw', encoding="UTF-8")
content = []
while True:
    line = f.readline()
    if not line: break
    content.append('filelists/wavs/' + line)
f.close()



a = open('filelists/ljs_audio_text_val_filelist.txt', 'w', encoding="UTF-8")
for i in content:
    a.write(i)
a.close()
