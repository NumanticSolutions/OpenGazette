
## OpenGazette : Docs

The initial motivation for this code was a minimal tool to directly convert a zipped patent gazette directly to a CSV file.

The zipped patent gazette typically consists of thousands of individual files, including HTML pages and GIF images. Uncompressed the gazette can be hundreds of megabytes in size.

In contrast, the CSV is single file derived from all issued patents and consists of just the identifier, the title, the inventor(s) and filed by information. For a single gazette this file can be on the order of half a megabyte.

This conversion makes use of a [```ZippedPatentGazette```](https://github.com/NumanticSolutions/OpenGazette/blob/main/opengazette/zipped_patent_gazette.py) class to handle the selective decompression of the gazette assets. For larger scale processing, for example when processing the gazettes for an entire year, it is efficient to only ever decompress single files of interest at a time.

In addition, the conversion uses the [```ParseGazetteHTML```](https://github.com/NumanticSolutions/OpenGazette/blob/main/opengazette/parse_gazette_html.py) class to parse the inidivual patent HTML files. This class uses the [Beatiful Soup](https://www.crummy.com/software/BeautifulSoup/) library.

Additional [source code](https://github.com/NumanticSolutions/OpenGazette/tree/main/opengazette) includes :

* ```example*``` files : which are simple examples based on the included [data files](https://github.com/NumanticSolutions/OpenGazette/tree/main/data)
* ```gazette*``` files : which are minimal command line programs which assume a downloaded [patent gazette](https://developer.uspto.gov/product/patent-official-gazettes-listing) for processing



