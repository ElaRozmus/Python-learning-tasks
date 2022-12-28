#WYRAŻENIE ASSERT

assert 1 == 1
# %%
assert 1 == 2
# %%

def test_sum():
    assert sum([1, 2, 3]) == 6, "Powinno być 6"

    
#

def test_min():
    assert min([1, 2, 3]) == 2, "powinno być☺ 1"

# %%


if __name__ == "__main__":
    test_sum()
    test_min()
    print("wszystko ok")
# %%

a = 4 
b = 0
#using assert to check for 0

print("the value of a/b is: ")
assert b != 0, "Zero Division Error"
print(a/b)
# %%
# initializin list of foods temperatures
batch = [40, 26, 39, 30, 25, 21, 15, 65]

# initializing cut temperatures
cut = 26

# using assert to check for temperatures greater the cut

for i in batch:
    assert i >= 26, "Batch is Rejected"
    print(str(i) + " O.K")
# %%
import random


rejectedBatch = []
AcceptBatch = []
batch = random.sample(range(150),64)
#print(batch)
# initializing cut temperatures
cut = 26

# using assert to check for temperatures greater the cut

for number in batch:
    if number in batch:
        assert number >= 26, "Batch is Rejected"
        rejectedBatch.append(number)
    else:
        AcceptBatch.append(number)
        
print(str(i) + " O.K")

