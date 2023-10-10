
import threading


def print_cube(num):
	# function to print cube of given num
	print ("welcome to thread1")
	print("Cube: {}" .format(num * num * num))


def print_square(num):
	# function to print square of given num
	print("Square: {}" .format(num * num))


	# creating thread
t1 = threading.Thread(target=print_square, args=(10,))
t2 = threading.Thread(target=print_cube, args=(10,))
print ("Thread start")
	# starting thread 1
t1.start()
	# starting thread 2
t2.start()

	# wait until thread 1 is completely executed
t1.join()
	# wait until thread 2 is completely executed
t2.join()

	# both threads completely executed
print("Done!")
