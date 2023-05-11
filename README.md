# Python-Tools
A collection of various tools that I have made, written in Python. Many are very specific in purpose due to them being created as-needed while working on other projects or solving classwork. 


# subnet_calculator
For doing calculations related to subnet design (written as tool for CS4121 subnet pre-lab)


subnet_calculator.py takes input from the console for first address as integer (i.e., 10.10.24.X, where X is the inputted value) and at least one integer as the requested host amount. It then determines if the user wants additional subnet host requests and will continue until user says they are finished.

It then displays the LANs in descending order of host amounts. 

[UPDATE]
Calculator still carries hardcoded "10.10.172" string related to the lab exercise, but now prints the following: 

> Number of hosts requested
  
> The number of bits needed
  
> Subnet Mask
  
> Network Address
  
> Gateway Address
  
> Broadcast Address
  
> Host Range
    
Below is an example of subnet_calculator in use:


![image](https://user-images.githubusercontent.com/67984700/199848842-34e38b0c-4441-48c9-8fc4-bf2b4d455f70.png)
