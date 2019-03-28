import random
import sys


class BullsAndCows():
	
	def contains(self, nums, x):	# return true if x present in nums
		if x in nums:
			return True
		else:
			return False
			
			
	def genSecretDigits(self, x):	# generate 4 digit array of ints (all unique)
		nums = []
		random.seed(x)
		
		while len(nums) < 4:
			temp = random.randint(0,9)
			if self.contains(nums, temp):
				pass
			else:
				nums.append(temp)
		return nums	
		
		
	def extractDigits(self, x):		# user int input -> list of str digits
		if x < 0:
			x = x * -1
		s = str(x)
		if len(s) < 4:
			while len(s) < 4:
				s = '0' + s
		l = list(s)
		nums = [int(x) for x in l]
		return nums
		
		
	def getNumofBulls(self, secret, guess):	# num of EXACT matches
		if len(guess) != len(secret):
			raise ValueError("Secret and guess should have same number of elements.")
		else:
			bulls = 0
			for x in range(len(guess)):
				if secret[x] == guess[x]:
					bulls += 1
		return bulls


	def getNumofCows(self, secret, guess):	# num of NON exact matches
		if len(guess) != len(secret):
			raise ValueError("Secret and guess should have same number of elements.")
		else:
			i = 0
			cows = 0
			for s in secret:	# iterate through each digit in secret
# 				print("current secret digit %d" % s)
				if self.contains(guess,s):	# if digits exists in guess
# 					print("digit match in guess %d" % s)
					if s == guess[i]:	# if bull
# 						print("it is a bull %d" % s)
						cows -= 1
						if guess.count(s) >= 2:	# if multiple counts of digit found
# 							print("multiple digit count %d" % s)
							if self.contains(guess[:i], s):
# 								print("guess lower bound %d" % s)
								cows += 1
					cows += 1
# 					print ("cow count %d" % cows)
				i += 1
		return cows	


	def playBullsandCows(self, i):		# play method
		secret = self.genSecretDigits(i)	# generate secret based on input seed
# 		print secret
		
		print("Hey you! Wanna play Bulls & Cows?")
		print("Let's get crackin!")
		attempt = 1						# init # of attempts
		guess = []
		
		while guess != secret:			# while not solved
			print("\n")
			if attempt > 5:				# check if 5 attempts exhausted
				ui = raw_input("Wanna give up? (y/n) ")
				if ui == 'y':			# user quits
					print("Thanks for playing. You took %d tries." % attempt)
					break
				else:					# user keeps trying
					pass
					print("\n")
				
			print("Guess #%d:" % attempt)
			g = int(input("Enter a 4 digit code: "))	# take user guess input
			if g >= 0:		# if +ve
				guess = self.extractDigits(g)
				if len(guess) <= 4:		# if input <=4 digits
					print("Bulls: %s" % self.getNumofBulls(secret, guess)),
					print(" Cows: %s" % self.getNumofCows(secret, guess))
				else:
					print("Must enter +ve integer, 4 digits long. Pls try again...")
			else:
				print("Must enter +ve integer, 4 digits long. Pls try again...")
			attempt += 1
			
		if guess == secret:
			print("\n")
			print("Congrats! You cracked the code in %d tries." % attempt)    
		
		
def main():
	bnc = BullsAndCows()
	bnc.playBullsandCows(200)
	# s = [5,1,9,6]
# 	g = [9,9,9,9]
# 	print("Bulls: %s" % bnc.getNumofBulls(s, g))
# 	print(" Cows: %s" % bnc.getNumofCows(s, g))
	
	
if __name__ == "__main__":
    main()
