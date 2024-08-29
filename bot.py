import pyautogui as py
import time
import keyboard
import pyperclip
import cv2
import numpy as np 


def go_to_page(page):           ### algorithm to reduce the amount of time it takes to reach specific pages in the master catalog
    n = page - 5 
    q, r = n // 2, n % 2
    print(n)
    print(q)
    print(r)
    if page >= 5:
        py.click(1533, 1330)
        if r == 1 and q > 0:
                for _ in range(q + 1):
                     py.click(1533, 1330)
                     time.sleep(4.5)
                py.click(1566, 1335)
                time.sleep(3.5)
        else:
             for _ in range(q + 1):
                        py.click(1533, 1330)
                        time.sleep(4.5)
    else:
        for _ in range(page):
              py.click(1566, 1335)
              time.sleep(4.5)

page = 11 
k = 10
while page < 180:
    
    while k < 100:
        print(page)
        print(k)
        pyperclip.copy('')
        py.moveTo(828, 344)
        py.dragTo(944, 373, .5, button='left')
        time.sleep(.3)
        keyboard.press_and_release('ctrl + c')
        time.sleep(.4)                          # initial check to see if the page is loaded
        check = pyperclip.paste()
        if check == '':
            time.sleep(30)
        pyperclip.copy('')


        go_to_page(page)

        
        py.click(1019, 361)
        time.sleep(1)
        for _ in range(k):
            keyboard.press_and_release('tab')
            time.sleep(.05)
        keyboard.press_and_release('enter')
        time.sleep(1)
        
        ### Color recognition to see what part is selected
        
        screenshot = py.screenshot()
        screenshot_np = np.array(screenshot)

        magenta = np.array([236, 224, 255])
        tolerance = np.array([13, 13, 13])  

        lower_mag = np.clip(magenta - tolerance, 0, 255)
        upper_mag = np.clip(magenta + tolerance, 0, 255)

        # Threshold the BGR image to get only magenta areas
        mask = cv2.inRange(screenshot_np, lower_mag, upper_mag)
        # cv2.imshow('Magenta Areas', mask)
        # time.sleep(.7)
        # py.click(800, 1424)
        # cv2.waitKey(1)
        # time.sleep(3)
        # cv2.destroyAllWindows()  # Close the window
        magenta_positions = np.where(mask == 255)

        # Calculate the mode position of magenta pixels
        magenta_mode_x = int(np.median(magenta_positions[1]))
        magenta_mode_y = int(np.median(magenta_positions[0]))

        py.moveTo(magenta_mode_x, magenta_mode_y)
        time.sleep(2)
        print(magenta_mode_x, magenta_mode_y)
        time.sleep(.4)
        py.doubleClick()
        time.sleep(6)

        # Copy the Vendor Part Number

        py.tripleClick(1072, 309)
        pyperclip.copy('')  
        keyboard.press_and_release('ctrl + c')
        time.sleep(0.1)  
        ven_part_num = pyperclip.paste()
        print(ven_part_num)
        time.sleep(.5)
        var = pyperclip.paste()
        if var == '':                                       # Checking if the part screen has loaded properly
            time.sleep(20)
            py.tripleClick(1048, 343)
            pyperclip.copy('')  
            keyboard.press_and_release('ctrl + c')
            time.sleep(0.1)  
            ven_part_num = pyperclip.paste()
            print(ven_part_num)

        # Copy the Description

        py.tripleClick(535, 536)
        pyperclip.copy('')  
        keyboard.press_and_release('ctrl + c')              
        time.sleep(0.1)  
        description = pyperclip.paste()
        print(description)
        time.sleep(.2)

        # Copy the Part Number

        py.tripleClick(473, 306)
        pyperclip.copy('')
        keyboard.press_and_release('ctrl + c')
        time.sleep(.1)
        part_num = pyperclip.paste()
        print(part_num)

        # Skip repeated part numbers that cause problems

        repeated = ['CS', 'SLV', 'BX']
        print("CS" in part_num or "SLV" in part_num or "BX" in part_num, 'if True repeated part_num if False unique part_num')
        if "CS" in part_num or "SLV" in part_num or "BX" in part_num:
            time.sleep(.3)
            py.click(282, 178)
            time.sleep(.6)
        else:
            hypen_removed = ''.join([char for char in part_num if char != '-'])

            if description == '':            # Skip the parts where there is no description               
                py.click(278, 178)
                time.sleep(12)
            else:

                # Copy the category(if there is one)

                py.tripleClick(1076, 364)
                pyperclip.copy('')  
                keyboard.press_and_release('ctrl + c')
                time.sleep(0.1)  
                category = pyperclip.paste()
                

                # search and save the image

                py.click(395, 4)
                time.sleep(.1)
                py.tripleClick(290, 131)
                keyboard.press_and_release('ctrl + a')
                if "HOOK" in description:                                   # adds "Hookit" to HOOK parts for better search results
                    combined_text = f"{ven_part_num} {description} Hookit"
                else:
                    combined_text = f"{ven_part_num} {description} {category}"
                print(combined_text)
                pyperclip.copy(combined_text)
                time.sleep(.1)
                keyboard.press_and_release('ctrl + v')
                keyboard.press_and_release('enter')
                time.sleep(10)


                ### Check to see if any images show up
                keyboard.press_and_release('ctrl + a')
                time.sleep(.5)
                keyboard.press_and_release('ctrl + c')
                time.sleep(.5)
                result = pyperclip.paste()

                if "looks like there" in result:
                    py.click(140, 17)
                    time.sleep(.3)
                    py.click(359, 217)
                    time.sleep(7)
                else:
                    ### Check to see if part number is in the description of the first image
                    py.rightClick(125, 383)
                    time.sleep(1.5)
                    py.click(223, 406)
                    time.sleep(1)
                    py.click(622, 15)
                    time.sleep(4)
                    py.rightClick(995, 128)
                    time.sleep(1)
                    py.click(1086, 146)
                    time.sleep(.7)
                    

                    py.click(863, 14)
                    time.sleep(5)
                    pyperclip.copy('')  
                    py.click(425, 656)
                    time.sleep(.5)
                    keyboard.press_and_release('ctrl + a')
                    time.sleep(0.5)
                    keyboard.press_and_release('ctrl + c')
                    time.sleep(.6)
                    page_content = pyperclip.paste()

                    py.click(969, 20)
                    py.click(395, 4)
                    py.click(389, 18)
                    time.sleep(1.9)
                    if part_num in page_content or hypen_removed in page_content:
                        py.rightClick(85, 336)
                        time.sleep(1)
                        py.click(203, 559)
                        time.sleep(1)
                        py.click(790, 506)
                        time.sleep(1)

                        # insert the image

                        py.click(135, 10)
                        time.sleep(1)
                        py.click(1863, 637)
                        time.sleep(3)
                        py.click(1275, 398)
                        time.sleep(1)
                        py.click(343, 166)
                        keyboard.press_and_release('enter')
                        time.sleep(.7)
                        py.click(2429, 1308)
                        time.sleep(.6)
                        py.click(359, 182)
                        time.sleep(1)

                        pyperclip.copy('')  
                        time.sleep(.5)
                        keyboard.press_and_release('ctrl + a')
                        time.sleep(0.5)
                        keyboard.press_and_release('ctrl + c')
                        time.sleep(.6)
                        unique_check = pyperclip.paste()
                        py.click(695, 156)
                        
                        if 'The Vendor Part Number' in unique_check:
                            time.sleep(.5)
                            py.click(285, 220)
                            time.sleep(1.3)
                        # delete the image from my computer

                        py.click(456, 1422)
                        time.sleep(.5)
                        py.click(700, 149)
                        keyboard.press_and_release('delete')
                        py.click(1019, 19)

                        pyperclip.copy('')
                    else:
                        py.click(139, 1)
                        time.sleep(.1)
                        py.click(283, 214)
                        time.sleep(5)
                    py.click(731, 22)
                    time.sleep(.7)
                    py.click(731, 22)
        time.sleep(5)
        k += 1
    page += 1