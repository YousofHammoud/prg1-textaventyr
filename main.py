print ("(Du är ett barn som vandrar öknen. Du har varit och köpt spannmål åt din familj och är på väg hem)")
print ("(Under din resa hemåt så finner du ett läger och ser en man sitta helt själv. Mannen har ett pack fyllt med böcker, och sitter vid en kittel. Han har inte ens lagt märke till dig. Det är inte förän du går till lägret som mannan lägger märke till dig)")

print ("Var hälsad denna natt å unga ökenvandrare.")
print ("Jag heter Zommoros, förr känd som en högt uppsatt forskare. Nu förvisad från kristall oasen.")

namn = input ("Vad må ditt namn vara barn? ")
print (f"Fred vare över dig å {namn}.")

print ("Jag har spenderat mina år av att sprida min kunskap. Nu när du står framför mig så önskar jag att få gen dig en del av min kunskap.")
print ("Jag kan läsa för dig en av två böcker. Aldrig har några öron fått ta del av frukten av dessa arbeten.")

print ("Den blåa boken handlar om allt det goda och fina av livet, och även alla former av goda, kärleksfulla och självlösa handlingar. dokumenterat från historia självt.")
print ("Den röda boken handlar om allt det onda och plågsamma av livet, och även alla former av onda, illvilliga och själviska handlingar. dokumenterat från historia självt.")

svar = input ("Jag läser endast en av de här skrifter för dig. Säg mig, vilken blir det? (Den blåa/Den röda)").lower()

if svar == "den blåa":
    print ("(Zommoros öppnar den blåa boken och börjar läsa högt ur den. Du lyssnar med spänning och lär dig om alla de goda handlingarna som människor har utfört genom historien. Du känner dig inspirerad och fylld av hopp.)")
    print (f"Å {namn}, Jag känner den starka hungern jag bär. Mitt föråd av spannmål är slut. Jag har suttit själv hungrig hela dagen och hela natten. Må du vara så generös att ge en svältande själ en del av det spannmål som du bär med dig.")
    svar = input ("(Du funderar över på vad du ska göra, din familj förväntar sig den mängden spannmål värt pengarna dem gav dig. Ska du ge en del av varorna till Zommoros? ((ge)/(ge inte)))").lower()
    if svar == "(ge)":
        print (f" Välsignelser vara över dig {namn}! Du har tagit lärdom från mig och gjort en sann osjälvisk, god och generös handling. Farväl {namn},och må du varndra en stig av det goda.")
        print ("(Du säger farväl till Zommoros och fortsätter din resa hemåt. Du är säker på att du känner igen ditt hem, du har ju trots allt gått denna väg vad som känns som hudratals gånger. Men du känner inte igen platsen, de gröna ängarna och de kristallklara floderna var inte där förut. Men du ser ändå din familj. Dem är överlyckliga att se dig. Du berättar om din resa. Sen lever ni lyckligt i alla era dagar.)")
        print ("(Så var sagan slut.)")
    elif svar == "(ge inte)":
        print (f"Jag tänker inte ifrågesätta ditt beslut. Men jag hoppas att du en dag kommer att förstå och känna medkänsla för den svältande själen. Jag bara hoppas att du får lärdom på ett lika milt sätt som att lyssna uppmärksamt på en högläsning av en bok. Farväl {namn}.")
        print ("(Du kommer hem till din familj, och med precis den mängden spannmål som du hade betalat för. När tiden kommer för att du skall gå på ännu en resa till marknaden så är det inte som det brukar vara. Den är helt tom på varor och folk. Du vänder dig till den enda personen du hittar där. Det är ett hungrit barn. Som förklarar för dig att en plötslig torka har drabbat området och det flesta handelsmän har flyttat sina affärer till andra riken. Du tvingas gå hem med tomma packfickor. Äntlingen så har den blåa bokens sanna läxa uppenbarats för dig.)")
        print ("(Så var sagan slut.)")

elif svar == "den röda":
    print ("(Zommoros öppnar den röda boken och börjar läsa högt ur den. Du lyssnar med ängslighet och lär dig om alla de onda handlingarna som människor har utfört genom historien. Du känner dig bekymrad och fylld av sorg.)")
    svar = input ("(Zommoros fyller en kanna med en svart främmande vätska. Han lägger fram två drykesbägare och fyller de med vätskan. Du litar inte på Zommoros och tror att han har hällt upp ett gift i bägarna. Han erbjuder att dricka från hans bägare först. Du känner dig säker på att om han faktiskt gör det så kommer han att dö. Tänker du låta han göra det eller tänker du stoppa honom? ((låt)/(låt inte))").lower()
    if svar == "(låt inte)":
        print ("()")