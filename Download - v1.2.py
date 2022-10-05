print('Youtube donwloader v1.2 script by Youssef Abdulaziz')

import os
print('Checking for dependencies...\n')

print('Checking complete!\n')



link = input('paste link here :' )
print('\nchoose format:\n1:audio [m4a]\n2:video [mp4]')
choice = input('\nselected format: ')

try:
        if(choice == "1"):
                os.system(f'yt-dlp -x --audio-format m4a {link}')
                files = os.listdir('.')
                for file in files:
                        pre, ext = os.path.splitext(file)
                        if(ext=='.webm'):
                                os.rename(file,f'{pre}.m4a')

        else:
                os.system(f"yt-dlp -x --format mp4 {link}")
        print('Download Successful!') 
except Exception as e:
	print(f'An err occurred\nerr: {e}')
	print('script unsuccessful')
