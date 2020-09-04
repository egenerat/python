import tarfile

if __name__ == "__main__":
    archive_filename = "foo.tar.gz"
    source_dir = "src"
    with tarfile.open(archive_filename, "w:gz") as tar:
        tar.add("src/file.txt", arcname="file.txt")
