"""
NimbusNote HTML To Md Conv
"""

import zipfile


def cnv_path(ph):
    if os.path.exists(ph):
        os.chdir(ph)
        for f in os.listdir(ph):
            if f.endswith('.zip'):
                fh = open(f, 'rb')
                z = zipfile.ZipFile(fh)
                for nm in z.namelist():
                    z.extract(nm, ph)
                    (nn, l) = f.split('.', maxsplit=1)
                    # print(lat2rus(nn))
                    print("Directory: %s" % os.getcwd())
                    # os.rename(nm, lat2rus(nn) + '.fb2')
                fh.close()


from markdownify import markdownify as md
import os, shutil, re


def nimbusNoteHtmlToMdConv1():
    def subf(v, pd, sh=0):
        if 'elem_type' in v and v['elem_type'] == 'folder':
            fn = os.path.join(pd, v['folder_name'])
            try:
                os.mkdir(fn)
            except:
                pass
            print(' ' * sh, v['folder_name'])
            for n in v["notes"]:
                nn = os.path.join(fn, n["note_title"].translate(str.maketrans("[]{}<>—", "()()()-", "!@#$%^&*+|\/:;")))
                suf, cnr = '', 0
                while os.path.isfile(nn + suf + ".md"):
                    cnr += 1
                    suf = f"_{cnr}"
                nn += suf + ".md"
                f = open(nn, mode="w", encoding="utf-8")
                cnt = n['content_data']
                for i in re.findall(r"#attacheloc:([^#]+)#", cnt):
                    for j in n["attach_list"]:
                        if j["attach_id"] == i:
                            pn = j["pathname"]
                            nm = os.path.basename(pn)
                            shutil.copyfile("D://sau//JP//NimbusNotes" + pn[1:], os.path.join(fn, nm))
                            cnt = cnt.replace(f"#attacheloc:{i}#", nm)
                            break

                f.write(md(cnt, heading_style="ATX"))
                f.close()
                print(' ' * (sh + 4), '>', n["note_title"], len(cnt))
            for j in v["subfolders"]:
                subf(j, fn, sh + 4)
        return

    ph = 'D://sau//PJ//NimbusNotes//All Notes'
    ou = 'D://sau//PJ//NimbusNotes//OUT_HTML'
    for f in os.scandir(ph):
        if f.is_dir():
            print('>', f.name)
        else:
            pass
        # for f in os.listdir(ph):
        #     if os.path.isfile(f):
        #         print('> ', f)
        #     else:
        #         print(f)
        # if f.endswith('.zip'):

    # f = open('D://sau//JP//NimbusNotes//sau270.json', 'r', encoding="utf-8")
    # for v in json.load(f):
    #     if 'elem_type' in v and v['elem_type'] == 'folder' and v['folder_name'] == 'User Folder':
    #         subf(v, 'D://sau//JP//NimbusNotes//OUT')

    return


def nimbusNoteHtmlToMdConv2():
    def exec_folder(ph, po):
        for f in os.scandir(ph):
            if f.is_dir():
                try:
                    os.mkdir(po + f.name)
                except:
                    pass
                exec_folder(f.name)
            else:
                if f.name.endswith('.zip'):
                    fh = open(f, 'rb')
                    z = zipfile.ZipFile(fh)
                    for nm in z.namelist():
                        z.extract(nm, ph)
                        (nn, l) = f.split('.', maxsplit=1)
                        # print(lat2rus(nn))
                        print("Directory: %s" % os.getcwd())
                        # os.rename(nm, lat2rus(nn) + '.fb2')
                    fh.close()
                print(f)


def nimbusNoteHtmlToMdConv3():
    def exec_folder(ph, po):
        for root, dirs, files in os.walk(ph):
            r = root.split('\\')
            if len(r) > 1:
                po = os.path.join(po, r[-1])
                try:
                    os.mkdir(po)
                except:
                    pass
            # print('>>', type(root))
            # for i in dirs:
            # print('>', dirs)
            for i in files:
                print(' ', i)

    exec_folder('D://sau//PJ//NimbusNotes//All Notes', 'D://sau//PJ//NimbusNotes//OUT_HTML')


def nimbusNoteHtmlToMdConv():
    pt = 'D://sau//PJ//NimbusNotes//TMP'
    ph = 'D://sau//PJ//NimbusNotes//All Notes'
    cp = po = 'D://sau//PJ//NimbusNotes//OUT_HTML'
    for root, dirs, files in os.walk(ph):
        r = root.split('\\')
        print(r)
        if len(r) > 1:
            cp = os.path.join(po, *r[1:])
            try:
                os.mkdir(cp)
            except FileExistsError:
                pass
        for f in files:
            if f.endswith('.zip'):
                # zipfile.ZipFile(os.path.join(ph, *(r[1:] + [f]))).extractall(pt)
                zipfile.ZipFile(os.path.join(ph, *(r[1:] + [f]))).extract('note.html', pt)
                fi = open(os.path.join(pt, 'note.html'), mode="r", encoding="utf-8")

                no = os.path.join(cp, f.replace('.zip', '.md'))
                fo = open(no, mode="w", encoding="utf-8")
                fo.write(md(fi.read(), heading_style="ATX"))
                fo.close()

                suf, cnr = '', 0
                # while os.path.isfile(nn + suf + ".md"):
                #     cnr += 1
                #     suf = f"_{cnr}"
                # nn += suf + ".md"
                # f = open(nn, mode="w", encoding="utf-8")
                # cnt = n['content_data']
                # for i in re.findall(r"#attacheloc:([^#]+)#", cnt):
                #     for j in n["attach_list"]:
                #         if j["attach_id"] == i:
                #             pn = j["pathname"]
                #             nm = os.path.basename(pn)
                #             shutil.copyfile("D://sau//JP//NimbusNotes" + pn[1:], os.path.join(fn, nm))
                #             cnt = cnt.replace(f"#attacheloc:{i}#", nm)
                #             break



nimbusNoteHtmlToMdConv()
