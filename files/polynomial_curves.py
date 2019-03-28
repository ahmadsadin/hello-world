def onCurve(pt, coef, t):
	temp = 0
	coef_rev = coef[::-1]
	for n in range(len(coef_rev)):
		temp = (coef_rev[n] * (pt[0] ** n)) + temp
	if abs(temp-pt[1]) < t:
		return True
	else:
		return False
	
		
def verifyInput(coef, t):
	if len(coef) < 1:
		raise ValueError("Coefficient list should have at least 1 element.")
	if t <= 0:
		raise ValueError("Curve thickness should be +ve.")
		
		
def drawCurve(coef, t, ch):
	verifyInput(coef, t)
	
	Y_LOW_BOUND = -10
	Y_UP_BOUND = 10+1
	
	if coef[-1] < -5:
		Y_LOW_BOUND = coef[-1] - 5
	if coef[-1] > 5:
		Y_UP_BOUND = coef[-1] + 5+1
# 	print Y_UP_BOUND
	
	y_range = list(range(Y_LOW_BOUND, Y_UP_BOUND))
	y_range.reverse()
	
	for y in y_range:
		for x in range(-10, 10+1):
			if onCurve([x,y],coef,t):
				print(ch),
			elif x==0 and y==Y_UP_BOUND-1:
				print("^"),
			elif ((x==0 and y>0) or (x==0 and y<0)) and onCurve([0,y],coef,t) == False \
			and (x==0 and y<=Y_UP_BOUND):
				print("|"),
			elif ((y==0 and x>0) or (y==0 and x<0)) and onCurve([x,0],coef,t) == False \
			and (y==0 and x!=10):
				print("-"),
			elif x==0 and y==0:
				print("+"),
			elif y==0 and x==10:
				print(">"),
			else:
				print(" "),	
		print("\n")	
			
			
def main():
	curve_coef = [0.1, 1, -8]
	thickness = 1.05
	drawCurve(curve_coef, thickness, "o")
	
	
if __name__ == "__main__":
    main()
    