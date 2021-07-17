# ONE-TIME PAD PYTHON FRAMEWORK (OTPy)

One-time pad (OTP) is a crypto algorithm where plaintext is combined with a random key. This encryption scheme is the only existing mathematically unbreakable encryption.<br/>
**Note:** Due to digital footprint this implementation of the encryption scheme should not be considered as unbreakable!

The resulting  ciphertext will be impossible to decrypt if the following conditions are met:

1.  The key must be random ([uniformly distributed](https://en.wikipedia.org/wiki/Discrete_uniform_distribution "Discrete uniform distribution")  and  independent of the plaincode).
2. Each subsequent cipher text should be as long as the previous ciphertext.
3. The plaincode must be at least as long as the key.
4. The key and the plaincode must be of an equal lenght.
5. The key must never be reused in whole or in part.
6. The key must be kept completely  secrecy  by the communicating parties.

**Is it truly unbreakable?** Yes and no. If used properly under strict rules - it is unbreakable by any modern machine or known technique.
Even a strong enough machine to brute-force every single possible combination, the original message cannot be determined from the ciphertext alone since all possible plaintexts are equally likely to be true.

In one-time pad cipher all calculations are performed by modular arithmetic. In most simple terms, one-time pad encryption scheme is an equation with two unknowns. To render useless various statistical and mathematical techniques, used  to guess/estimate these unknowns, the encryption scheme uses the modulo 10 arithmetic operation. In Layman's terms the modular 10 arithmetic works similar to counting hours on a decimal clock (0-9). If the hand of our clock is at 7 and we add 4 by advancing clockwise, we pass the 0 marker and arrive at 1. Likewise, when the clock hand is at 2 and we subtract 4, advancing anticlockwise, we arrive at 8. Thus seeing the hand of our lock at any given position - we have no idea where the hand came from and which two clock positions are added or subtracted. 

## Requirements
Python 3.6

## How to run
```
git clone https://github.com/SubXi/otpy-framework.git
python3.6 main.py
```

## Notes

**Audio settings:**

All audio files are stored in otpy-framework\vo <br/>
Custom audio files should be mono, resampled to 22050Hz, exported as .WAV - 16-bit PCM

**Checkerboard:**

Custom checkerboard is supported with slight changes to the below code in func.py line 18:
```python
T = [["68", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
     ["",   "A", "T", "", "O",  "N", "E", "", "S",  "I", "R"],
     ["2",  "B", "C", "D", "F", "G", "H", "J", "K", "L", "M"],
     ["6",  "P", "Q", "U", "V", "W", "X", "Y", "Z", "/", " "]]
```

## Sources:

http://users.telenet.be/d.rijmenants/papers/one_time_pad.pdf <br/>
https://www.cryptomuseum.com/crypto/otp/index.htm <br/>
http://users.telenet.be/d.rijmenants/en/onetimepad.htm <br/>

## Disclaimer

This program is created for educational purposes only. 
When you download and use this program - you use it at your own discretion and risk and I will not be held accountable for any damages inflicted by its use.

**Each and every individual, which uses this program, should use it in accordance to local and international laws!**
