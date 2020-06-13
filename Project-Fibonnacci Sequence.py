
# coding: utf-8

# # Fibonnacci Sequence

# I am writing a program to generate a Fibonacci sequence to the Nth number, where N could be any value

# In[1]:


def fibo_seq(N):
    
    result = []
    a = 1
    b = 1
    
    for i in range(N):
        result.append(a)
        a,b = b,a+b
    return result


# In[2]:


fibo_seq(100)

