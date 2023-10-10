s = input("File name: ")
end = s.split(".")[-1]
match end:
    case "pdf":
        print("application/pdf")
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "txt":
        print("text/plain")
    case "gif":
        print("image/gif")
    case "zip":
        print("application/x-7Z-compressed")
    case "png":
        print("image/png")