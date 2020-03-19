class IO:
    supportedsrcs=["console","file"]
    def read(src):
        if src not in IO.supportedsrcs:
            print("not supported")
        else:
            print("read from",src)

print(IO.supportedsrcs)
IO.read("filessssss")



