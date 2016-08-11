import tornado
import tornado.ioloop
import tornado.web
import os, uuid
import time

PORT               = 8888
UPLOADS            = "uploads/"
DEBUG              = False
SECURITY_RANDOMIZE = False
ADD_TIME_TO_FILE   = True #Only for not randomized


class Upload(tornado.web.RequestHandler):
    def post(self):
        fileinfo = self.request.files['filearg'][0]
        if (DEBUG): print("fileinfo is"), fileinfo
        fname = fileinfo['filename']
        split = os.path.splitext(fname)
        prename = split[0] if (not SECURITY_RANDOMIZE) else uuid.uuid4()
        if (ADD_TIME_TO_FILE): prename += time.strftime("-%Y%m%d-%H%M%S")
        cname = str(prename) + split[1]
        fh = open(UPLOADS + cname, 'wb')
        fh.write(fileinfo['body'])
        self.finish("[+] Done")


application = tornado.web.Application([
        (r"/upload", Upload),
        ], debug=DEBUG)


if __name__ == "__main__":
    application.listen(PORT)
    tornado.ioloop.IOLoop.instance().start()
