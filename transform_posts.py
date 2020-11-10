'''Transform the posts markdown to update the metadata as Gatsby wants it.

Example usage:

python transform_posts --in blogs --out content/posts

'''
import os
import shutil

class Header:

    def __init__(self, category=None):
        self.attrs = {}
        self.category = category
    
    def add_line(self, line):
        line = line.strip()
        if not line:
            return
        i = line.index(':')
        if i < 0:
            return
        attr, value = line[0:i].strip(), line[i+1:].strip()
        self.attrs[attr] = value
    
    def fix_attrs(self):
        attrs = {}
        attrs.update(self.attrs)
        tags = attrs.get('tags')
        if tags:
            attrs['tags'] = [t.strip() for t in tags.split(',')]
        
        attrs['template'] = 'post'
        attrs['categories'] = [self.category] if self.category else []
        if 'cover' not in attrs:
            if self.category:
                attrs['cover'] = '../images/categories/%s.png' % self.category

        return attrs

    def get_lines(self):
        lines = []
        for key, value in self.fix_attrs().items():
            if isinstance(value, list):
                lines.append('%s:' % key)
                for val in value:
                    lines.append('  - %s' % val)
                continue
            lines.append('%s: %s' % (key, value))
        return lines

def transform_file(filename, outfilename, category=None):
    with open(filename, 'r') as postf:
        with open(outfilename, 'w') as outf:
            header = None
            header_read = False
            for line in postf:
                if header_read:
                    outf.write(line)
                    continue
                if line.strip().startswith('---'):
                    if not header:
                        header = Header(category=category)
                    else:

                        #try:
                        date_str = get_post_update_time(filename)
                        if date_str:
                            header.attrs['date'] = date_str
                        # except Exception as e:
                        #     print(e)
                        header_lines = ['---'] + header.get_lines() + ['---']
                        for hline in header_lines:
                            outf.write('%s\n' % hline)
                        header_read = True
                elif header and not header_read:
                    header.add_line(line)
                else:
                    outf.write(line)

def transform_files(srcdir, destdir):
    if not os.path.exists(destdir):
        os.makedirs(destdir)
    for fname in os.listdir(srcdir):
        if fname.startswith('.'):
                continue
        full_name = os.path.join(srcdir, fname)
        if os.path.isdir(full_name):
            transform_files(full_name, os.path.join(destdir, fname))
        else:
            if full_name.lower().endswith('.md'):
                transform_file(full_name, os.path.join(destdir, fname), category=os.path.basename(srcdir))
            else:
                shutil.copyfile(full_name, os.path.join(destdir, fname))


def get_post_update_time(file_name):
    from pathlib import Path
    path = Path(file_name)

    git_repo = None
    while path.parent != path:
        parent = path.parent
        if parent.joinpath('.git').exists():
            git_repo = parent
        path = path.parent
    if not git_repo:
        print('File %s is not inside git repo.' % file_name)
        return None
    
    import subprocess
    result = subprocess.check_output(
        ['git', 'log', '-1', r'--format=%ci', os.path.relpath(file_name, git_repo.absolute())],
        cwd=git_repo)
    if result:
        return result.decode('utf-8').strip()
    return None



if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser('Transform blog posts')
    parser.add_argument('--in', help='Blogs input directory', dest='input')
    parser.add_argument('--out', help='Output directory for the transformed files', dest='out')

    args = parser.parse_args()
    if args.input and args.out:
        transform_files(args.input, args.out)

