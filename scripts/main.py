from maplib import Parameter, Prefix, RDFType, Template

kl = Prefix("https://knowledgelinks.io/")

template = Template(
    iri = kl.suf("skills/five-whys"),
    parameters=[],
    instances=[]
)

def main():
    print(f"Hello from five-whys-skill!\n{template}")


if __name__ == "__main__":
    main()
