wrong = 0
sed = 0  # Sum of absolute errors
mred = 0  # Sum of relative errors
nmed_sum = 0  # Sum of normalized errors
P_max = 65025  # Maximum possible error (255 * 255)

for i in range(256):
    for j in range(256):
        z = i * j  # Accurate product

        a = DTB(i)  # Convert i to binary
        b = DTB(j)  # Convert j to binary

        y = Binary_Multiply8(a, b)  # Approximate product from the  multiplier
        pdt = decimal(y)  # Convert the approximate result to decimal

        diff = abs(pdt - z)  # Absolute error
        sed += diff  # Add absolute error to the sum

        # Calculate the normalized error for NMED
        normalized_error = diff / P_max
        nmed_sum += normalized_error  # Add to NMED sum

        # If accurate product is not zero, calculate RED for MRED
        if z != 0:
            red = diff / z
            mred += red

        # Count the number of wrong outputs (non-zero error)
        if diff != 0:
            wrong += 1

# Calculate total combinations (27 * 27 = 729)
total_combinations = (i + 1) * (j + 1)

# Mean Error Distance (MED)
#med = sed / total_combinations

# Normalized Mean Error Distance (NMED)
Nmed = nmed_sum / total_combinations  # Mean of normalized errors

# Error rate percentage (ERT)
ert = (wrong / total_combinations) * 100

# Correct results count and percentage (PSRT)
crt = total_combinations - wrong
psrt = (crt / total_combinations) * 100

# Mean Relative Error Distance (MRED)
Mred = mred / total_combinations

# Print results
print("Total combinations:", total_combinations)
print("Total wrong combinations:", wrong)
print("Total correct combinations:", crt)
print("Error rate (ERT):", ert, "%")
print("Pass rate (PSRT):", psrt, "%")
print("Total error distance (SED):", sed)
#print("Mean error distance (MED):", med)
print("Normalized mean error distance (NMED):", Nmed)
print("Mean relative error distance (MRED):", Mred)
