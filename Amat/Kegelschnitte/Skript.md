## Parametrisierung des Kreises und der Ellipse

Wir sehen einen Punkt, und seine Bewegung scheint auf den ersten Blick schwierig mathematisch zu beschreiben zu sein. Er scheint keiner simplen Funktion zu folgen.  

Vielleicht ist es einfacher, dem Punkt zu folgen, wenn wir ein Koordinatensystem darüberlegen. Dazu werden wir noch die Koordinaten des Punktes betrachten, zusammen mit der vergangenen Zeit.  

Wir sehen jetzt klar und deutlich, dass der Punkt einen Kreis abgefahren hat – in einer Zeit von **6.28**. Diese Zeit hier steht nicht in Sekunden. Sie ist der **Winkel des Punktes zur X-Achse** und ist nicht in Grad, sondern im **Bogenmaß** angegeben.  

Das Bogenmaß ist sehr einfach vorzustellen: Es stellt den Winkel dar, den ein Punkt zur X-Achse hat, nachdem man die Länge des Maßes am Kreisrand entlanggelaufen ist. Deshalb beträgt das Bogenmaß momentan **6.28** oder **2π**, weil dieser Kreis der **Einheitskreis** ist und der Punkt einmal um den Kreis gegangen ist.  

Wie würden wir jetzt jedoch die Bewegung dieses Punktes als eine Funktion der Zeit beschreiben?  
Man nimmt die **x- und y-Koordinaten** des Punktes und macht aus jeder Koordinatenkomponente eine **Funktion der Zeit**, um herauszufinden, wo sich der Punkt zu einer bestimmten Zeit $$t$$ befindet. Dazu muss jede Koordinate mit der entsprechenden Funktion berechnet werden, indem man $$t$$ einsetzt.  

Dieser Prozess nennt sich **Parametrisierung**.  
Was wir jetzt machen möchten, ist, den Einheitskreis zu parametrisieren.  
Die dazugehörigen Funktionen sind:  

$$x = \cos(t), \quad y = \sin(t)$$

Dies können wir überprüfen, indem wir sie in die Kreisgleichung für einen Kreis mit Radius $$1$$ einsetzen.  
Das Ergebnis stimmt, da es der **trigonometrischen Identität** entspricht.  

Dies mag jedoch etwas abstrakt erscheinen, weshalb wir dies nochmals intuitiver veranschaulichen wollen.  

Dazu nehmen wir einen Ausschnitt aus dem Einheitskreis und einen zufälligen Punkt auf ihm.  
Nun zeichnen wir die Koordinaten des Punktes ein und verschieben die grüne Linie, um ein **rechtwinkliges Dreieck** zu bilden, wobei die **Hypotenuse der Radius** des Kreises ist und somit die Länge $$1$$ besitzt.  

Die **x-Koordinate** des Punktes ist damit die Länge einer Seite in diesem Dreieck. Wenn wir annehmen, dass $$t$$ der Winkel des Punktes zur X-Achse ist, dann ergibt sich für die Ankathete die Länge $$\cos(t)$$ – also unsere x-Koordinate.  
Die **y-Koordinate** folgt auf die gleiche Weise aus der Definition der trigonometrischen Funktionen in einem rechtwinkligen Dreieck.  

Damit haben wir unsere vorher formell berechnete Vermutung bestätigt, da nach dem Satz des Pythagoras gilt:

$$\cos^2(t) + \sin^2(t) = 1$$

---

### Parametrisierung der Ellipse

Schauen wir uns nun auch die **Parametrisierung einer Ellipse** an, da diese viele Anwendungen in der Wissenschaft hat.  

Wir nehmen die Gleichung einer Ellipse, für die wir nun Funktionen der Zeit für $$x$$ und $$y$$ finden wollen.  
Wenn wir die Funktionen des Kreises ausprobieren und einsetzen, sehen wir, dass dies nicht aufgeht, da sich die Längen der **Scheitelachsen** nicht wegkürzen.  

Das bringt uns jedoch schon weiter:  
Wir können in der x-Koordinate den Faktor $$a$$ einbeziehen, was ermöglicht, dass sich $$a^2$$ wegkürzt.  
Dasselbe machen wir mit der y-Koordinate und dem Faktor $$b$$.  

Das führt uns zur bekannten trigonometrischen Identität, die wir bereits kennen, und damit haben wir die **Parametrisierung der Ellipse** gefunden:

$$x = a \cos(t), \quad y = b \sin(t)$$

Wir können diese Parametrisierung auch intuitiver zeigen.  

Nehmen wir ein Koordinatensystem und setzen $$a = b = 1$$.  
Dann vereinfacht sich unsere Parametrisierung wieder zur des Einheitskreises.  

Nun können wir anfangen, den Kreis in x-Richtung herauszuziehen, indem wir $$a$$ vergrößern.  
Dasselbe tun wir mit der y-Koordinate, indem wir $$b$$ verändern.  

Wenn $$a$$ und $$b$$ den gleichen Wert haben, erhalten wir wieder einen Kreis – nur größer, da er gleichmäßig in beide Richtungen gedehnt wurde.  

---

### Warum Parametrisierung?

Warum sollte man sich jedoch die Mühe machen, diese komplizierte Parametrisierung zu berechnen?  

Sie ist sehr hilfreich beim Zeichnen von Formen im Koordinatensystem, die **keine Funktionen** sein können – wie die Ellipse.  

Wenn wir versuchen, eine Ellipse als Funktion darzustellen, bekommen wir zwei Funktionen wegen der quadrierten y-Variable.  
Dann müssten wir alle Berechnungen **getrennt** für den oberen und unteren Teil der Ellipse durchführen – was mühsam wäre.  

Der bessere Weg ist die **Parametrisierung**, die uns eine kontinuierliche Ellipse ohne Spezialfälle liefert.  

Deshalb werden Parametrisierungen oft genutzt, um **kontinuierliche kreisähnliche Bewegungen in der Physik** zu beschreiben – auf eine davon gehen wir jetzt ein.  

---

### Beispiel: Umlaufbahn der Erde

Dazu müssen wir jedoch zuerst beobachten, was passiert, wenn wir in der Zeit weitergehen als **6.28**.  
Wie schon gesagt, ist dies nur der Winkel, weshalb der Punkt einfach nochmals die Ellipse abfährt.  

Ein gutes Beispiel, um das zu zeigen, ist die **Bewegung der Erde auf ihrer Umlaufbahn um die Sonne**.  

Dies scheint auf den ersten Blick **kein Kreis** zu sein – das liegt aber nur daran, dass die Umlaufbahn der Erde eine **Exzentrizität von etwa 1 %** besitzt.  
Wir sehen, dass sich die Längen der Haupt- und Nebenachsen nur um **0.6** unterscheiden, was jedoch immer noch viel ist, da diese Angaben in **Millionen Kilometern** stehen.  

Deshalb lassen wir die Umlaufbahn der Erde ein wenig mehr wie eine Ellipse aussehen, indem wir sie leicht zusammendrücken – ohne die numerischen Werte zu verändern.  

Dann können wir die Erde einzeichnen, zusammen mit der Zeit, die hier für ein Jahr angepasst ist.  
In den trigonometrischen Funktionen wird mit $$2\pi$$ multipliziert, damit die volle Umdrehung von $$t_0$$ bis $$t_1$$ genau **ein Jahr** entspricht.  

Nach etwa einem Siebtel des Jahres ist gerade März, und wir können beobachten, wie sich die Erde mit zunehmender Zeit während des Jahres bewegt.  

Dies ist jedoch ein **vereinfachtes Modell**, da angenommen wurde, dass sich die Erde **gleich schnell** während des ganzen Jahres bewegt – was nach den **Keplerschen Gesetzen** nicht stimmt.  
Der Effekt ist hier aber klein, da die Exzentrizität sehr gering ist.  
