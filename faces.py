def main():
    face = input ()
    print (convert(face) )
def convert (text ):
    text = text.replace(":)","🙂")
    text = text.replace(":(","🙁")
    return text
main ()
