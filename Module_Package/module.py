# Import and use the system module
import sys
print(sys.platform)
print(sys.maxsize)

# Import the gematry module amd create an alias for module called geo
sys.path.append("d:\\python\\python_practice\\Module\\modules") # Add new module path in system path
import geomatry as geo
print(geo.dis(1,1,5,5))
print(geo.slope(5,9,6,2))

# Print the path of module
print(sys.path)