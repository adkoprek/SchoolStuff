### Allgemein

Das Sierpienski Dreieck ist ein Fraktal, welches schon seit der Antike zu dekorativen Zwecken gebraucht wurde. Es wurde jedoch nach ihm benannt, weil er der gewesen ist, welcher das Fraktal formalisiert hat und dazu Berechnungen aufgestellt hat. Ein Fraktal ist eine geometrische Figur, welche definitionsmäßig detaillierte Strukturen enthält, mit jeder Skalierung. Im Fall des Sierpienski Dreiecks wiederholt sich das ursprüngliche Dreieck immer wieder in kleineren Unterdreiecken.

### Konstruktion

Es kann kanstruiert werden mit der Methode der Entfernung von Dreiecken.

1. Man beginnt mit einem gleichseitigem Dreieck

2. Man unterteilt das Dreieck in 4 grösstmögliche Kongruente Dreiecke und man entfährnt das Mittlere Dreieck.

3. Man weiderholt den Prozess mit jedem Dreieck eine **unedlich** viele male

### Fläche mit der Annehrung an Unendlichkeit

Weil man diesen rekursiven Prozess unendlich mal wiederholt nimmt man immer $\frac{1}{4}$ der Fläche weg, bei jeder Iteration bleiben damit nur $\frac{3}{4}$ der Fläche des Dreiecks vor dieser Iteration übrig. Die Fläche des Dreiecks konvergiert bzw. nährt isch 0 an

$$
\lim_{n \to \infty} \left( \frac{3}{4} \right)^n = 0
$$

### Der Umfang

Der Umfang des Dreiecks ist hingegen unendlich gross **Beweiss**

### Dimensionalität

Die Dimension einer regelmäsige euklidische Form kann definiert werden, indem man  alle Seiten mit einem Faktor ($S$) $\frac{1}{2}$ skaliert und untersucht, um welchen *Massefaktor $(M)$* die Form skaliert wird. 

- Für ein Linie, die man halbiert ist der Massefaktor gleich dem Teilungsfaktor $\frac{1}{2}= \left( \frac{1}{2} \right) ^1$

- Ein Quadrat kann man in vierteln, die resultierende Quadradate werden halbierte Seiten von dem originalen Quadrat haben $\frac{1}{4}=(\frac{1}{2})^2$

- Ein Quader kann man achtteln, die resultierenden Quader werden ebenfalls halb so lange seiten wie der original Quader $\frac{1}{8}=(\frac{1}{2})^3$

Aus den obigen Berechnungen kann man die folgende Berechnung abgeleitet werden für die Dimension ($d$)

$$
M=S^d
$$

Das Sierpienski Dreieck kann gedrittelt ($M$) werden, wobei jedes Dreieck um einen Faktor ($S$) von $\frac{1}{2}$ kleiner ist, als das Orignielle. Es git also

$$
\left( \frac{1}{2} \right)^d=\frac{1}{3} \space <=> \space 2^d=3
$$

Die Dimension kann mit einem Logarithmus ermittelt werden

$$
log_2(3) \approx 1.585
$$
