def lens(list):
	return sorted(list,key=lambda x:len(x))
print lens(['python','perl','java','c','haskell','ruby'])
