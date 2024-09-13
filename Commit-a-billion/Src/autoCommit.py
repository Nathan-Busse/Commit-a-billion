import os

ip = int(input("How many commits do you want to push for this one? \n"))
autoPush = input("Would you like to Auto git push when commited? (y/n) \n")

for i in range(ip):
	# os.system('git commit --allow-empty -m "New Commit at: $(date)"')
	os.system(f'git commit --allow-empty -m "Commit {i} of {ip}"')	

print("Commited " + str(ip) + " times")

if autoPush == "y":
	os.system('git push')
	
# git commit --allow-empty -m "New Commit at: $(date)"

# Project Author: Nathan_Busse
# Inspired by VirejDesani's Commited repo. The very first and only GitHub repository to reach 3 million commits!
