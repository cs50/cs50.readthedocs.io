# CS50 Certificates

CS50 Certificates is a web app at [certificates.cs50.io](https://certificates.cs50.io/) via which students, if eligible, can download their very own certificates from CS50's courses and events like CS50x Puzzle Day. Each certificate has a unique URL as well as a 2D barcode via which the certificate's authenticity can be confirmed. (CS50 does not, however, verify recipients' identities.) Certificates can be downloaded as PDFs for printing (in Letter or A4 size) or as PNGs for social media.

Underneath the hood, the certificates are implemented with HTML, CSS, and JavaScript. And CS50 uses [Puppeteer](https://pptr.dev/) (a "headless" version of Chrome) to render them as PDFs and PNGs.
