import time
f1 = open("ocr.txt", "r")
str = f1.read()
for i in str:
	if i == '$': time.sleep(0)
	elif i == '%': time.sleep(0)
	elif i == '@': time.sleep(0)
	elif i == '_': time.sleep(0)
	elif i == '^': time.sleep(0)
	elif i == '(': time.sleep(0)
	elif i == ')': time.sleep(0)
	elif i == '[': time.sleep(0)
	elif i == ']': time.sleep(0)
	elif i == '*': time.sleep(0)
	elif i == '!': time.sleep(0)
	elif i == '+': time.sleep(0) 
	elif i == '#': time.sleep(0)
	elif i == '{': time.sleep(0)
	elif i == '}': time.sleep(0)
	elif i == '&': time.sleep(0)
	elif i == ' ': time.sleep(0)
	elif i == '\n': time.sleep(0)
	else: print(i)
