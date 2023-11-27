# NTT
To run the code, run the following commands:
```
cd cooleyTukey
python3 run_script.py minusoneRing.py input.txt
python3 run_script.py plusoneRing.py input.txt

```

To see the middle steps of butterfly diagram, uncomment the print statements in the butterfly function in main.py (line 109-110)

## Next Steps:
- [ ] Implement NTT for \mathbb{Z}[x]/(x^n+1) ring
- [ ] Do even-odd indexing for butterfly diagram
- [ ] Inverse NTT implementation on both rings
- [ ] Have a program to take two polynomials as input and output their product using NTT implementations
- [ ] Complete the report