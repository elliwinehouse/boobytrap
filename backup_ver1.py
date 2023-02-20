import os, time

source = ['C:\kingsoft', 'C:\\Users\ellicom\Pictures\luke-mckeown-nlyWZtWTzCo-unsplash.jpg']
target_dir = 'E:\Backup'
target = target_dir + os.sep + time.strftime('%Y%m%d_%H%M%S') + '.zip'

zip_command = "zip -qr {} {}".format(target, ' '.join(source))

if os.system(zip_command) == 0: print('Резервная копия успешно создана в', target)
else: print('Создание резервной копии НЕ УДАЛОСЬ')









