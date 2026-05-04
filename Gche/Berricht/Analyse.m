keys = (-1:15)';
values = [3.71 3.83 3.92 4.0 4.07 4.15 4.22 4.3 4.37 4.44 4.51 4.58 4.66 4.74 4.83 4.94 5.056]';
transformed_values = exp(values);

least = (keys' * keys \ keys' * transformed_values)

fit = (0.1 * transformed_values) / least
plot(keys, transformed_values);
hold on;
plot(keys, fit)

