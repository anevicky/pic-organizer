import exifread
import os
#opens file that will write the output
logfile = open('code_output_2.txt', 'a')
#function that prints output and saves it in a file
def save_code(printed_text):
    logfile.write(printed_text + '\n')
    print(printed_text)

def move_image_datetime(filepath, root_dest):
    # gets file extension
    extension = os.path.splitext(filepath)[1]

    # check if file is an image
    if extension in ('.png','.jpeg','.jpg', '.JPG', '.PNG'):
        with open(filepath, 'rb') as image:
            # extracting the exif metadata
            tags = exifread.process_file(image)

        if 'EXIF DateTimeOriginal' in tags:
            DateTime = tags['EXIF DateTimeOriginal']

            value = str(DateTime)

            #replacing ':' for '-' in DateTime value
            new_file_name = value.replace(':', '-')

            date_str1 = value.split(':')
            # gets only the year part of the str
            date_year = date_str1[0]
            # creating a folder for the file
            destination_folder = root_dest + os.sep + str(date_year)
            filepathdes = destination_folder + os.sep + new_file_name + extension

            if not os.path.exists(destination_folder):
                # Create target Directory
                os.mkdir(destination_folder)
                text_create_directory = destination_folder + " was created."
                save_code(text_create_directory)
            # renames the image with the date
            #check if file already exists in filepathdes
            if not os.path.exists(filepathdes):
                os.rename(filepath, filepathdes)
                text_imagefile_moved = filepath + " is an image and it was renamed and moved to " + filepathdes
                save_code(text_imagefile_moved)
            #in case filepathdes already exists:
            else:
                count = 1
                #define variable that will be checked and altered with while. It cant be filepathdes bc we dont want to modify it
                duplicate_image=filepathdes
                #loops to check if the image exists. While this is TRUE, it will modify the variable duplicate_image
                # until it is not duplicate anymore -FALSE-  to exit loop
                while os.path.exists(duplicate_image):
                    duplicate_image = destination_folder + os.sep + new_file_name + "(" + str(count) + ")" + extension
                    count += 1
                #when condition for loop is FALSE - meaning that file does not exists - it moves the image renamed to new destination
                os.rename(filepath,duplicate_image)
                text_duplicate = filepath + " is likely a duplicate image and it was renamed and moved to " + duplicate_image
                save_code(text_duplicate)

        else:
            whatsapp_folder = root_dest + os.sep + 'WhatsApp Images'
            filename = os.path.split(filepath)
            whatsappImage = whatsapp_folder + os.sep + filename[1]
            if not os.path.exists(whatsapp_folder):
                # Create target Directory
                os.mkdir(whatsapp_folder)
                text_whatsapp_folder = whatsapp_folder + ' was created.'
                save_code(text_whatsapp_folder)

            #move to WhatsApp folder
            if not os.path.exists(whatsappImage):
                os.rename(filepath, whatsappImage)
                text_whatsapp_file = filepath + ' does not have DateTimeOriginal tag and it was moved to ' + whatsappImage
                save_code(text_whatsapp_file)

            else:
                count = 1
                # define variable that will be checked and altered with while. It cant be filepathdes bc we dont want to modify it
                duplicate_image = whatsappImage
                # loops to check if the image exists. While this is TRUE, it will modify the variable duplicate_image
                # until it is not duplicate anymore -FALSE-  to exit loop
                while os.path.exists(duplicate_image):
                    duplicate_image = whatsapp_folder + os.sep + filename[1] + "(" + str(count) + ")" + extension
                    count += 1
                # when condition for loop is FALSE - meaning that file does not exists - it moves the image renamed to new destination
                os.rename(filepath, duplicate_image)
                text_duplicate = filepath + " is likely a duplicate image and it was renamed and moved to " + duplicate_image
                save_code(text_duplicate)

    else:
        not_an_image = filepath + " is not an image."
        save_code(not_an_image)

source = r'C:\Users\ane_c\Downloads'
destination = r'C:\Users\ane_c\Desktop\Fotos'
# iterating through directory and moving files code
for subdir, dirs, files in os.walk(source):
    for file in files:
        filepath = subdir + os.sep + file
        move_image_datetime(filepath, destination)

logfile.close()