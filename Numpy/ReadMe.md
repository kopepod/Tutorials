# Numpy tutorial

1. Grid

```python
x, y = numpy.meshgrid(numpy.linspace(0.5,1.5,10), numpy.linspace(0.5,1.5,10))
```

2. string to array

```python
numpy.fromstring(TSP_KF[1:-1], dtype = int, sep = ',');
```

3. append in for loop: Error -- numpy append
you must specify 'dtype=object' when creating the ndarray

```python
Y = numpy.array([], dtype = object)

for 
	Y = numpy.append(Y,[1,2,3])
	
	
Y = numpy.asarray(Y, dtype = float)
```

4. dataframe vectors to numpy array

```python
X = numpy.array(list(X), dtype = numpy.float32)
```

5. Choice subsample matrix Replace bootstrap

```python
numpy.random.choice(5,3,replace = False)
```

6. sampling with linear spacing
```python
numpy.linspace(0.2, 0.8, N)

numpy.arange(0,10,3)
```

7. plot histogram

```python

from matplotlib import pyplot
import numpy

rng = numpy.random.RandomState(10)  # deterministic random data
x0 = numpy.hstack((rng.normal(size=1000), rng.normal(loc=5, scale=2, size=1000)))

rng = numpy.random.RandomState(12)  # deterministic random data
x1 = numpy.hstack((rng.normal(size=1000), rng.normal(loc=10, scale=4, size=1000)))

_ = pyplot.hist(x0, bins='auto', alpha = 0.5, label = "Distribution 0")
_ = pyplot.hist(x1, bins='auto', alpha = 0.5, label = "Distribution 1")

pyplot.title("Histogram with 'auto' bins")
pyplot.legend(loc = "upper right")
pyplot.show()
```

8. save load array
```ptyhon
numpy.savetxt(TPATH + inputfile,y,delimiter=",");
numpy.savetxt('X.txt', X , delimiter =',', fmt = '%f');

numpy.loadtxt(File, dtype = float, delimiter =',')

```

9. string without scientific notation
```python
numpy.format_float_positional(1e-07)
```

10. vstack
```python
y = numpy.array(numpy.zeros((0,768)), dtype = object)
for i , xi in enumerate(x):
	xi = numpy.fromstring(xi, dtype = numpy.float32, sep = ',',  precision = 6, suppress_small = True);
	y = numpy.vstack((y, xi)).astype(numpy.float32);
```


11. array to string
```python
x = numpy.array2string(x, precision = 6, separator =',', suppress_small = True);
x = x.replace("\n","")
```

12. Piecewise plot

```
from matplotlib import pyplot
import numpy

x = numpy.arange(0., 10., 0.2)
y = numpy.piecewise(x, [x < 2, (x >=2) & (x < 4), x >= 4], [0, 0.5, 0])
pyplot.plot(x,y)
pyplot.show()

```
13. print format
```python
numpy.set_printoptions(suppress = True, precision = 3)
```

14. sort
```python
idx = numpy.argsort(numpy.linalg.norm(fv-FV, axis = 1))
```
