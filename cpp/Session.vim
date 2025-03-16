let SessionLoad = 1
if &cp | set nocp | endif
let s:cpo_save=&cpo
set cpo&vim
imap <C-_> 
imap <M-Up> <M-Up>
imap <M-Down> <S-F11>
imap <S-F11> <S-F11>
imap <S-F10> <S-F10>
imap <F10> <F10>
imap <S-F9> <S-F9>
imap <F9> <F9>
imap <S-F7> <S-F7>
imap <F7> <F7>
imap <S-F6> :q!
imap <F6> :q
map! <F5> <F5>
imap <S-F4> <S-F4>
imap <F4> <F4>
imap <F17> <F17>
imap <S-F3> <S-F3>
imap <F3> <F3>
imap <S-F2> <S-F2>
map! <F2> :up
imap <F1> <F1>
cnoremap <C-S> 
lnoremap <C-L> 
noremap! <C-L> 
nmap <silent> <NL> :call Move_down()
vmap <silent> <NL> :m<Home>silent! <End>'>+1gv
nmap <silent>  :call Move_up()
vmap <silent>  :m<Home>silent! <End>'<-2gv
nnoremap  :call Comment()
vnoremap  :call Comment()
nmap \] 
noremap \\c :echo getcurpos()
nnoremap \\t i#TODOj
vmap \] 
nnoremap \[ gI//:s+////++e+
nnoremap \Z 0xj0
nnoremap \z 0i#j0
nnoremap \w di"hPlxxW
nnoremap \q ciW""PW
nnoremap <silent> \9 :call VerSwitch(9)
nnoremap <silent> \8 :call VerSwitch(8)
nnoremap <silent> \7 :call VerSwitch(7)
nnoremap <silent> \6 :call VerSwitch(6)
nnoremap <silent> \5 :call VerSwitch(5)
nnoremap <silent> \4 :call VerSwitch(4)
nnoremap <silent> \3 :call VerSwitch(3)
nnoremap <silent> \2 :call VerSwitch(2)
nnoremap <silent> \1 :call VerSwitch(1)
nnoremap <silent> \f :call VerList()
nnoremap <silent> \n :call VerInc()
noremap \s :call Ls()
noremap \v :call Ve()
noremap \l :set cul!
noremap \c :set cuc!
nnoremap \u g~iWW
vmap \, <gv
vmap \. >gv
nmap <silent> \k :co.-1
nmap <silent> \j :co.
nnoremap \P "0P
nnoremap \p "0p
nnoremap \O O
nnoremap \o o
nnoremap \  i‗r
nnoremap \J i
vnoremap \d "_d
nnoremap \d "_dd
nnoremap \S dd"0P
nmap \X \<Up>
nmap <silent> \<Up> :call Ft2a()
nmap \x \<Down>
nmap <silent> \<Down> :call Fta()
nnoremap \<F3> :!cd "%:p:h" && make
nmap <silent> \T :call term_start("bash -c py",{"term_name": "python", "term_finish": "close"})
nmap <silent> \t :call term_start("bash",{"term_name": "bash", "term_finish": "close"})
xmap gx <Plug>NetrwBrowseXVis
nmap gx <Plug>NetrwBrowseX
nmap <silent> gh :call Move_hor(-1)
nmap <silent> gl :call Move_hor(1)
nnoremap gO Oj
nnoremap go ok
nnoremap gb go
nmap z/ 
vmap z/ 
nmap zX <M-Up>
nmap zx <S-F11>
nnoremap <C-_> :call Comment()
xnoremap <silent> <Plug>NetrwBrowseXVis :call netrw#BrowseXVis()
nnoremap <silent> <Plug>NetrwBrowseX :call netrw#BrowseX(netrw#GX(),netrw#CheckIfRemote(netrw#GX()))
vnoremap <C-_> :call Comment()
nmap <F15> \v
nmap <silent> <C-Left> :call Move_hor(-1)
nmap <silent> <C-Right> :call Move_hor(1)
vmap <C-Left> <gv
vmap <C-Right> >gv
nmap <silent> <C-Up> :call Move_up()
nmap <silent> <C-K> :call Move_up()
vmap <silent> <C-Up> :m<Home>silent! <End>'<-2gv
vmap <silent> <C-K> :m<Home>silent! <End>'<-2gv
nmap <silent> <C-Down> :call Move_down()
nmap <silent> <C-J> :call Move_down()
vmap <silent> <C-Down> :m<Home>silent! <End>'>+1gv
vmap <silent> <C-J> :m<Home>silent! <End>'>+1gv
nmap <F16> :set list!
nnoremap <S-F12> :up:!!
nmap <M-Up> :call Ft2()
nmap <M-Down> <S-F11>
nnoremap <S-F11> :call Ft()
vmap <S-F10> <S-F10>
nmap <S-F10> :cprev	
vmap <F10> <F10>
nmap <F10> :cnext	
vmap <S-F9> <S-F9>
nmap <S-F9> :cclose	
vmap <F9> <F9>
nmap <F9> :copen
nmap <S-F8> :set rnu!
nmap <F8> :set nu!
vmap <S-F7> <S-F7>
nnoremap <S-F7> :G 
vmap <F7> <F7>
nnoremap <silent> <F7> :call SynSwitch()
vmap <S-F6> :q!
nmap <S-F6> :q!
vmap <F6> :q
nmap <F6> :q
map <silent> <F5> :VimrcReload
nmap <S-F4> :VimrcEdit2
nmap <F4> :VimrcEdit
vmap <F17> <F17>
nnoremap <F17> :!make TARGET="%:t:r"
vmap <S-F3> <S-F3>
nnoremap <S-F3> :!make debug
vmap <F3> <F3>
nnoremap <F3> :!make
vmap <S-F2> <S-F2>
nnoremap <S-F2> :!make ctags
map <F2> :up
vmap <F1> <F1>
nmap <F1> :mks!
tmap <F2> N
lnoremap  
noremap!  
cnoremap  
imap  
iabbr -#_ —
iabbr #p #!/usr/bin/python3
iabbr #b #!/usr/bin/bash
let &cpo=s:cpo_save
unlet s:cpo_save
set keymap=russian-jcukenwin
set autoindent
set autowrite
set background=dark
set backspace=indent,eol,start
set noequalalways
set expandtab
set fileencodings=ucs-bom,utf-8,default,latin1
set helplang=ru
set highlight=8:SpecialKey,~:EndOfBuffer,@:NonText,d:Directory,e:ErrorMsg,i:IncSearch,l:Search,m:MoreMsg,M:ModeMsg,n:LineNr,a:LineNrAbove,b:LineNrBelow,N:CursorLineNr,G:CursorLineSign,O:CursorLineFold,r:Question,s:StatusLine,S:StatusLineNC,c:VertSplit,t:Title,v:Visual,V:VisualNOS,w:WarningMsg,W:WildMenu,f:Folded,F:FoldColumn,A:DiffAdd,C:DiffChange,D:DiffDelete,T:DiffText,>:SignColumn,-:Conceal,B:SpellBad,P:SpellCap,R:SpellRare,L:SpellLocal,+:Pmenu,=:PmenuSel,x:PmenuSbar,X:PmenuThumb,*:TabLine,#:TabLineSel,_:TabLineFill,!:CursorColumn,.:CursorLine,o:ColorColumn,q:QuickFixLine,z:StatusLineTerm,Z:StatusLineTermNC,M:Type
set imsearch=0
set incsearch
set langmap=ёйцукенгшщзхъфывап��олджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРО��ДЖЭЯЧСМИТЬБЮ;`qwertyuiop[]asdfghjkl\\;'zxcvbnm\\,.~QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>
set mouse=a
set path=.,/usr/include,,,/usr/include/x86_64-linux-gnu,/usr/include/c++/11
set printencoding=cp1251
set printfont=courier:h8
set printoptions=left:5pc
set ruler
set scrolloff=2
set sessionoptions=blank,buffers,folds,help,options,tabpages,winsize,terminal,sesdir
set shiftwidth=4
set shortmess=filnxtToOSI
set showcmd
set showmatch
set smartindent
set smarttab
set softtabstop=4
set spelllang=ru_yo,en_us
set splitright
set statusline=%t\ %<[%{expand('%:p:~:h')}]%(\ %h%m%r%)%(\ %k%)\ \ w%{winnr()}\ b%{winbufnr(0)}\ %=%b\ 0x%B\ \ %-12.(%l,%c%V%)\ %P
set suffixes=.bak,~,.swp,.o,.info,.aux,.log,.dvi,.bbl,.blg,.brf,.cb,.ind,.idx,.ilg,.inx,.out,.toc
set ttimeoutlen=100
set wildmenu
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
exe "cd " . escape(expand("<sfile>:p:h"), ' ')
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
argglobal
%argdel
$argadd ~/cpp/vec.hpp
edit ~/cpp/vec.hpp
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
wincmd _ | wincmd |
split
1wincmd k
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 97 + 97) / 195)
exe '2resize ' . ((&lines * 23 + 24) / 49)
exe 'vert 2resize ' . ((&columns * 97 + 97) / 195)
exe '3resize ' . ((&lines * 23 + 24) / 49)
exe 'vert 3resize ' . ((&columns * 97 + 97) / 195)
argglobal
balt storage.hpp
nnoremap <buffer> \> Icin >> $a;$
nnoremap <buffer> \< Icout << $a << endl;$
nmap <buffer> \b \}
nmap <buffer> \{ \}
let s:cpo_save=&cpo
set cpo&vim
nnoremap <buffer> \} :s/\(\S\)\s*$/\1 /eA <BS>{ <BS>}kI
lnoremap <buffer> " Э
lnoremap <buffer> # №
lnoremap <buffer> $ ;
lnoremap <buffer> & ?
lnoremap <buffer> ' э
lnoremap <buffer> , б
lnoremap <buffer> . ю
lnoremap <buffer> / .
lnoremap <buffer> : Ж
lnoremap <buffer> ; ж
lnoremap <buffer> < Б
lnoremap <buffer> > Ю
lnoremap <buffer> ? ,
lnoremap <buffer> @ "
lnoremap <buffer> A Ф
lnoremap <buffer> B И
lnoremap <buffer> C С
lnoremap <buffer> D В
lnoremap <buffer> E У
lnoremap <buffer> F А
lnoremap <buffer> G П
lnoremap <buffer> H Р
lnoremap <buffer> I Ш
lnoremap <buffer> J О
lnoremap <buffer> K Л
lnoremap <buffer> L Д
lnoremap <buffer> M Ь
lnoremap <buffer> N Т
lnoremap <buffer> O Щ
lnoremap <buffer> P З
lnoremap <buffer> Q Й
lnoremap <buffer> R К
lnoremap <buffer> S Ы
lnoremap <buffer> T Е
lnoremap <buffer> U Г
lnoremap <buffer> V М
lnoremap <buffer> W Ц
lnoremap <buffer> X Ч
lnoremap <buffer> Y Н
lnoremap <buffer> Z Я
lnoremap <buffer> [ х
lnoremap <buffer> ] ъ
lnoremap <buffer> ^ :
lnoremap <buffer> ` ё
lnoremap <buffer> a ф
lnoremap <buffer> b и
lnoremap <buffer> c с
lnoremap <buffer> d в
lnoremap <buffer> e у
lnoremap <buffer> f а
lnoremap <buffer> g п
lnoremap <buffer> h р
lnoremap <buffer> i ш
lnoremap <buffer> j о
lnoremap <buffer> k л
lnoremap <buffer> l д
lnoremap <buffer> m ь
lnoremap <buffer> n т
lnoremap <buffer> o щ
lnoremap <buffer> p з
lnoremap <buffer> q й
lnoremap <buffer> r к
lnoremap <buffer> s ы
lnoremap <buffer> t е
lnoremap <buffer> u г
lnoremap <buffer> v м
lnoremap <buffer> w ц
lnoremap <buffer> x ч
lnoremap <buffer> y н
lnoremap <buffer> z я
lnoremap <buffer> { Х
lnoremap <buffer> } Ъ
lnoremap <buffer> ~ Ё
iabbr <buffer> ci cin >> x;Fxs
iabbr <buffer> coe cout << x << endl;Fxs
iabbr <buffer> cod cout << x << ' ';Fxs
iabbr <buffer> co cout << x;Fxs
iabbr <buffer> #I #include <iostream>using namespace std;int main() {}O
iabbr <buffer> fc char f() {}2k$F)i
iabbr <buffer> fl long f() {}2k$F)i
iabbr <buffer> fi int f() {}2k$F)i
iabbr <buffer> fv void f() {}2k$F)i
iabbr <buffer> {{ { <BS>}kI
iabbr <buffer> }} { <BS>}kI
iabbr <buffer> ifel if() {} else {}4k$F)i
iabbr <buffer> iff if() {}2k$F)i
iabbr <buffer> fork for(int k = 0; k < _; k++) F_s
iabbr <buffer> forj for(int j = 0; j < _; j++) F_s
iabbr <buffer> fori for(int i = 0; i < _; i++) F_s
iabbr <buffer> prF printf("\n");fflush(stdout);kF\i
iabbr <buffer> prp printf("%p\n", _);F_s
iabbr <buffer> prfe printf("%e\n", _);F_s
iabbr <buffer> prfg printf("%g\n", _);F_s
iabbr <buffer> prf printf("%f\n", _);F_s
iabbr <buffer> prs printf("%s\n", _);F_s
iabbr <buffer> prc printf("%c\n", _);F_s
iabbr <buffer> prx printf("%x\n", _);F_s
iabbr <buffer> prl printf("%ld\n", _);F_s
iabbr <buffer> pri printf("%d\n", _);F_s
iabbr <buffer> prn printf("\n");F\i
iabbr <buffer> prt printf("");<Left><Left><Left>
iabbr <buffer> #m #include <math.h>
iabbr <buffer> #l #include <stdlib.h>
iabbr <buffer> #h #include <stdio.h>#include <stdlib.h>
iabbr <buffer> #i #include <stdio.h>int main() {}O
let &cpo=s:cpo_save
unlet s:cpo_save
setlocal keymap=russian-jcukenwin
setlocal noarabic
setlocal autoindent
setlocal backupcopy=
setlocal balloonexpr=
setlocal nobinary
setlocal nobreakindent
setlocal breakindentopt=
setlocal bufhidden=
setlocal buflisted
setlocal buftype=
setlocal cindent
setlocal cinkeys=0{,0},0),0],:,0#,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=
setlocal comments=sO:*\ -,mO:*\ \ ,exO:*/,s1:/*,mb:*,ex:*/,://
setlocal commentstring=/*%s*/
setlocal complete=.,w,b,u,t,i
setlocal concealcursor=
setlocal conceallevel=0
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
setlocal nocursorline
setlocal cursorlineopt=both
setlocal define=^\\s*#\\s*define
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal expandtab
if &filetype != 'cpp'
setlocal filetype=cpp
endif
setlocal fixendofline
set foldcolumn=1
setlocal foldcolumn=1
setlocal foldenable
setlocal foldexpr=0
setlocal foldignore=#
setlocal foldlevel=0
set foldmarker=//>,//<
setlocal foldmarker=//>,//<
set foldmethod=marker
setlocal foldmethod=marker
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=foldtext()
setlocal formatexpr=
setlocal formatoptions=croql
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal formatprg=
setlocal grepprg=
setlocal iminsert=0
setlocal imsearch=0
setlocal include=^\\s*#\\s*include
setlocal includeexpr=
setlocal indentexpr=
setlocal indentkeys=0{,0},0),0],:,0#,!^F,o,O,e
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255
setlocal keywordprg=
setlocal nolinebreak
setlocal nolisp
setlocal lispwords=
setlocal nolist
setlocal listchars=
setlocal makeencoding=
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal modeline
setlocal modifiable
setlocal nrformats=bin,octal,hex
set number
setlocal number
setlocal numberwidth=4
setlocal omnifunc=ccomplete#Complete
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal quoteescape=\\
setlocal noreadonly
setlocal norelativenumber
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal scrolloff=-1
setlocal shiftwidth=4
setlocal noshortname
setlocal showbreak=
setlocal sidescrolloff=-1
setlocal signcolumn=auto
setlocal smartindent
setlocal softtabstop=4
setlocal nospell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=ru_yo,en_us
setlocal spelloptions=
setlocal statusline=
setlocal suffixesadd=
setlocal swapfile
setlocal synmaxcol=3000
if &syntax != 'cpp'
setlocal syntax=cpp
endif
setlocal tabstop=8
setlocal tagcase=
setlocal tagfunc=
setlocal tags=
setlocal termwinkey=
setlocal termwinscroll=10000
setlocal termwinsize=
setlocal textwidth=0
setlocal thesaurus=
setlocal thesaurusfunc=
setlocal noundofile
setlocal undolevels=-123456
setlocal varsofttabstop=
setlocal vartabstop=
setlocal virtualedit=
setlocal wincolor=
setlocal nowinfixheight
setlocal nowinfixwidth
setlocal wrap
setlocal wrapmargin=0
let s:l = 20 - ((19 * winheight(0) + 23) / 47)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 20
normal! 054|
wincmd w
argglobal
if bufexists("main.cpp") | buffer main.cpp | else | edit main.cpp | endif
balt storage.hpp
nnoremap <buffer> \> Icin >> $a;$
nnoremap <buffer> \< Icout << $a << endl;$
nmap <buffer> \b \}
nmap <buffer> \{ \}
let s:cpo_save=&cpo
set cpo&vim
nnoremap <buffer> \} :s/\(\S\)\s*$/\1 /eA <BS>{ <BS>}kI
lnoremap <buffer> " Э
lnoremap <buffer> # №
lnoremap <buffer> $ ;
lnoremap <buffer> & ?
lnoremap <buffer> ' э
lnoremap <buffer> , б
lnoremap <buffer> . ю
lnoremap <buffer> / .
lnoremap <buffer> : Ж
lnoremap <buffer> ; ж
lnoremap <buffer> < Б
lnoremap <buffer> > Ю
lnoremap <buffer> ? ,
lnoremap <buffer> @ "
lnoremap <buffer> A Ф
lnoremap <buffer> B И
lnoremap <buffer> C С
lnoremap <buffer> D В
lnoremap <buffer> E У
lnoremap <buffer> F А
lnoremap <buffer> G П
lnoremap <buffer> H Р
lnoremap <buffer> I Ш
lnoremap <buffer> J О
lnoremap <buffer> K Л
lnoremap <buffer> L Д
lnoremap <buffer> M Ь
lnoremap <buffer> N Т
lnoremap <buffer> O Щ
lnoremap <buffer> P З
lnoremap <buffer> Q Й
lnoremap <buffer> R К
lnoremap <buffer> S Ы
lnoremap <buffer> T Е
lnoremap <buffer> U Г
lnoremap <buffer> V М
lnoremap <buffer> W Ц
lnoremap <buffer> X Ч
lnoremap <buffer> Y Н
lnoremap <buffer> Z Я
lnoremap <buffer> [ х
lnoremap <buffer> ] ъ
lnoremap <buffer> ^ :
lnoremap <buffer> ` ё
lnoremap <buffer> a ф
lnoremap <buffer> b и
lnoremap <buffer> c с
lnoremap <buffer> d в
lnoremap <buffer> e у
lnoremap <buffer> f а
lnoremap <buffer> g п
lnoremap <buffer> h р
lnoremap <buffer> i ш
lnoremap <buffer> j о
lnoremap <buffer> k л
lnoremap <buffer> l д
lnoremap <buffer> m ь
lnoremap <buffer> n т
lnoremap <buffer> o щ
lnoremap <buffer> p з
lnoremap <buffer> q й
lnoremap <buffer> r к
lnoremap <buffer> s ы
lnoremap <buffer> t е
lnoremap <buffer> u г
lnoremap <buffer> v м
lnoremap <buffer> w ц
lnoremap <buffer> x ч
lnoremap <buffer> y н
lnoremap <buffer> z я
lnoremap <buffer> { Х
lnoremap <buffer> } Ъ
lnoremap <buffer> ~ Ё
iabbr <buffer> ci cin >> x;Fxs
iabbr <buffer> coe cout << x << endl;Fxs
iabbr <buffer> cod cout << x << ' ';Fxs
iabbr <buffer> co cout << x;Fxs
iabbr <buffer> #I #include <iostream>using namespace std;int main() {}O
iabbr <buffer> fc char f() {}2k$F)i
iabbr <buffer> fl long f() {}2k$F)i
iabbr <buffer> fi int f() {}2k$F)i
iabbr <buffer> fv void f() {}2k$F)i
iabbr <buffer> {{ { <BS>}kI
iabbr <buffer> }} { <BS>}kI
iabbr <buffer> ifel if() {} else {}4k$F)i
iabbr <buffer> iff if() {}2k$F)i
iabbr <buffer> fork for(int k = 0; k < _; k++) F_s
iabbr <buffer> forj for(int j = 0; j < _; j++) F_s
iabbr <buffer> fori for(int i = 0; i < _; i++) F_s
iabbr <buffer> prF printf("\n");fflush(stdout);kF\i
iabbr <buffer> prp printf("%p\n", _);F_s
iabbr <buffer> prfe printf("%e\n", _);F_s
iabbr <buffer> prfg printf("%g\n", _);F_s
iabbr <buffer> prf printf("%f\n", _);F_s
iabbr <buffer> prs printf("%s\n", _);F_s
iabbr <buffer> prc printf("%c\n", _);F_s
iabbr <buffer> prx printf("%x\n", _);F_s
iabbr <buffer> prl printf("%ld\n", _);F_s
iabbr <buffer> pri printf("%d\n", _);F_s
iabbr <buffer> prn printf("\n");F\i
iabbr <buffer> prt printf("");<Left><Left><Left>
iabbr <buffer> #m #include <math.h>
iabbr <buffer> #l #include <stdlib.h>
iabbr <buffer> #h #include <stdio.h>#include <stdlib.h>
iabbr <buffer> #i #include <stdio.h>int main() {}O
let &cpo=s:cpo_save
unlet s:cpo_save
setlocal keymap=russian-jcukenwin
setlocal noarabic
setlocal autoindent
setlocal backupcopy=
setlocal balloonexpr=
setlocal nobinary
setlocal nobreakindent
setlocal breakindentopt=
setlocal bufhidden=
setlocal buflisted
setlocal buftype=
setlocal cindent
setlocal cinkeys=0{,0},0),0],:,0#,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=
setlocal comments=sO:*\ -,mO:*\ \ ,exO:*/,s1:/*,mb:*,ex:*/,://
setlocal commentstring=/*%s*/
setlocal complete=.,w,b,u,t,i
setlocal concealcursor=
setlocal conceallevel=0
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
setlocal nocursorline
setlocal cursorlineopt=both
setlocal define=^\\s*#\\s*define
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal expandtab
if &filetype != 'cpp'
setlocal filetype=cpp
endif
setlocal fixendofline
set foldcolumn=1
setlocal foldcolumn=1
setlocal foldenable
setlocal foldexpr=0
setlocal foldignore=#
setlocal foldlevel=0
set foldmarker=//>,//<
setlocal foldmarker=//>,//<
set foldmethod=marker
setlocal foldmethod=marker
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=foldtext()
setlocal formatexpr=
setlocal formatoptions=croql
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal formatprg=
setlocal grepprg=
setlocal iminsert=0
setlocal imsearch=0
setlocal include=^\\s*#\\s*include
setlocal includeexpr=
setlocal indentexpr=
setlocal indentkeys=0{,0},0),0],:,0#,!^F,o,O,e
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255
setlocal keywordprg=
setlocal nolinebreak
setlocal nolisp
setlocal lispwords=
setlocal nolist
setlocal listchars=
setlocal makeencoding=
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal modeline
setlocal modifiable
setlocal nrformats=bin,octal,hex
set number
setlocal number
setlocal numberwidth=4
setlocal omnifunc=ccomplete#Complete
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal quoteescape=\\
setlocal noreadonly
setlocal norelativenumber
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal scrolloff=-1
setlocal shiftwidth=4
setlocal noshortname
setlocal showbreak=
setlocal sidescrolloff=-1
setlocal signcolumn=auto
setlocal smartindent
setlocal softtabstop=4
setlocal nospell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=ru_yo,en_us
setlocal spelloptions=
setlocal statusline=
setlocal suffixesadd=
setlocal swapfile
setlocal synmaxcol=3000
if &syntax != 'cpp'
setlocal syntax=cpp
endif
setlocal tabstop=8
setlocal tagcase=
setlocal tagfunc=
setlocal tags=
setlocal termwinkey=
setlocal termwinscroll=10000
setlocal termwinsize=
setlocal textwidth=0
setlocal thesaurus=
setlocal thesaurusfunc=
setlocal noundofile
setlocal undolevels=-123456
setlocal varsofttabstop=
setlocal vartabstop=
setlocal virtualedit=
setlocal wincolor=
setlocal nowinfixheight
setlocal nowinfixwidth
setlocal wrap
setlocal wrapmargin=0
let s:l = 1 - ((0 * winheight(0) + 11) / 23)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 0
wincmd w
argglobal
if bufexists("storage.hpp") | buffer storage.hpp | else | edit storage.hpp | endif
balt main.cpp
nnoremap <buffer> \> Icin >> $a;$
nnoremap <buffer> \< Icout << $a << endl;$
nmap <buffer> \b \}
nmap <buffer> \{ \}
let s:cpo_save=&cpo
set cpo&vim
nnoremap <buffer> \} :s/\(\S\)\s*$/\1 /eA <BS>{ <BS>}kI
lnoremap <buffer> " Э
lnoremap <buffer> # №
lnoremap <buffer> $ ;
lnoremap <buffer> & ?
lnoremap <buffer> ' э
lnoremap <buffer> , б
lnoremap <buffer> . ю
lnoremap <buffer> / .
lnoremap <buffer> : Ж
lnoremap <buffer> ; ж
lnoremap <buffer> < Б
lnoremap <buffer> > Ю
lnoremap <buffer> ? ,
lnoremap <buffer> @ "
lnoremap <buffer> A Ф
lnoremap <buffer> B И
lnoremap <buffer> C С
lnoremap <buffer> D В
lnoremap <buffer> E У
lnoremap <buffer> F А
lnoremap <buffer> G П
lnoremap <buffer> H Р
lnoremap <buffer> I Ш
lnoremap <buffer> J О
lnoremap <buffer> K Л
lnoremap <buffer> L Д
lnoremap <buffer> M Ь
lnoremap <buffer> N Т
lnoremap <buffer> O Щ
lnoremap <buffer> P З
lnoremap <buffer> Q Й
lnoremap <buffer> R К
lnoremap <buffer> S Ы
lnoremap <buffer> T Е
lnoremap <buffer> U Г
lnoremap <buffer> V М
lnoremap <buffer> W Ц
lnoremap <buffer> X Ч
lnoremap <buffer> Y Н
lnoremap <buffer> Z Я
lnoremap <buffer> [ х
lnoremap <buffer> ] ъ
lnoremap <buffer> ^ :
lnoremap <buffer> ` ё
lnoremap <buffer> a ф
lnoremap <buffer> b и
lnoremap <buffer> c с
lnoremap <buffer> d в
lnoremap <buffer> e у
lnoremap <buffer> f а
lnoremap <buffer> g п
lnoremap <buffer> h р
lnoremap <buffer> i ш
lnoremap <buffer> j о
lnoremap <buffer> k л
lnoremap <buffer> l д
lnoremap <buffer> m ь
lnoremap <buffer> n т
lnoremap <buffer> o щ
lnoremap <buffer> p з
lnoremap <buffer> q й
lnoremap <buffer> r к
lnoremap <buffer> s ы
lnoremap <buffer> t е
lnoremap <buffer> u г
lnoremap <buffer> v м
lnoremap <buffer> w ц
lnoremap <buffer> x ч
lnoremap <buffer> y н
lnoremap <buffer> z я
lnoremap <buffer> { Х
lnoremap <buffer> } Ъ
lnoremap <buffer> ~ Ё
iabbr <buffer> ci cin >> x;Fxs
iabbr <buffer> coe cout << x << endl;Fxs
iabbr <buffer> cod cout << x << ' ';Fxs
iabbr <buffer> co cout << x;Fxs
iabbr <buffer> #I #include <iostream>using namespace std;int main() {}O
iabbr <buffer> fc char f() {}2k$F)i
iabbr <buffer> fl long f() {}2k$F)i
iabbr <buffer> fi int f() {}2k$F)i
iabbr <buffer> fv void f() {}2k$F)i
iabbr <buffer> {{ { <BS>}kI
iabbr <buffer> }} { <BS>}kI
iabbr <buffer> ifel if() {} else {}4k$F)i
iabbr <buffer> iff if() {}2k$F)i
iabbr <buffer> fork for(int k = 0; k < _; k++) F_s
iabbr <buffer> forj for(int j = 0; j < _; j++) F_s
iabbr <buffer> fori for(int i = 0; i < _; i++) F_s
iabbr <buffer> prF printf("\n");fflush(stdout);kF\i
iabbr <buffer> prp printf("%p\n", _);F_s
iabbr <buffer> prfe printf("%e\n", _);F_s
iabbr <buffer> prfg printf("%g\n", _);F_s
iabbr <buffer> prf printf("%f\n", _);F_s
iabbr <buffer> prs printf("%s\n", _);F_s
iabbr <buffer> prc printf("%c\n", _);F_s
iabbr <buffer> prx printf("%x\n", _);F_s
iabbr <buffer> prl printf("%ld\n", _);F_s
iabbr <buffer> pri printf("%d\n", _);F_s
iabbr <buffer> prn printf("\n");F\i
iabbr <buffer> prt printf("");<Left><Left><Left>
iabbr <buffer> #m #include <math.h>
iabbr <buffer> #l #include <stdlib.h>
iabbr <buffer> #h #include <stdio.h>#include <stdlib.h>
iabbr <buffer> #i #include <stdio.h>int main() {}O
let &cpo=s:cpo_save
unlet s:cpo_save
setlocal keymap=russian-jcukenwin
setlocal noarabic
setlocal autoindent
setlocal backupcopy=
setlocal balloonexpr=
setlocal nobinary
setlocal nobreakindent
setlocal breakindentopt=
setlocal bufhidden=
setlocal buflisted
setlocal buftype=
setlocal cindent
setlocal cinkeys=0{,0},0),0],:,0#,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=
setlocal comments=sO:*\ -,mO:*\ \ ,exO:*/,s1:/*,mb:*,ex:*/,://
setlocal commentstring=/*%s*/
setlocal complete=.,w,b,u,t,i
setlocal concealcursor=
setlocal conceallevel=0
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
setlocal nocursorline
setlocal cursorlineopt=both
setlocal define=^\\s*#\\s*define
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal expandtab
if &filetype != 'cpp'
setlocal filetype=cpp
endif
setlocal fixendofline
set foldcolumn=1
setlocal foldcolumn=1
setlocal foldenable
setlocal foldexpr=0
setlocal foldignore=#
setlocal foldlevel=0
set foldmarker=//>,//<
setlocal foldmarker=//>,//<
set foldmethod=marker
setlocal foldmethod=marker
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=foldtext()
setlocal formatexpr=
setlocal formatoptions=croql
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal formatprg=
setlocal grepprg=
setlocal iminsert=0
setlocal imsearch=0
setlocal include=^\\s*#\\s*include
setlocal includeexpr=
setlocal indentexpr=
setlocal indentkeys=0{,0},0),0],:,0#,!^F,o,O,e
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255
setlocal keywordprg=
setlocal nolinebreak
setlocal nolisp
setlocal lispwords=
setlocal nolist
setlocal listchars=
setlocal makeencoding=
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal modeline
setlocal modifiable
setlocal nrformats=bin,octal,hex
set number
setlocal number
setlocal numberwidth=4
setlocal omnifunc=ccomplete#Complete
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal quoteescape=\\
setlocal noreadonly
setlocal norelativenumber
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal scrolloff=-1
setlocal shiftwidth=4
setlocal noshortname
setlocal showbreak=
setlocal sidescrolloff=-1
setlocal signcolumn=auto
setlocal smartindent
setlocal softtabstop=4
setlocal nospell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=ru_yo,en_us
setlocal spelloptions=
setlocal statusline=
setlocal suffixesadd=
setlocal swapfile
setlocal synmaxcol=3000
if &syntax != 'cpp'
setlocal syntax=cpp
endif
setlocal tabstop=8
setlocal tagcase=
setlocal tagfunc=
setlocal tags=
setlocal termwinkey=
setlocal termwinscroll=10000
setlocal termwinsize=
setlocal textwidth=0
setlocal thesaurus=
setlocal thesaurusfunc=
setlocal noundofile
setlocal undolevels=-123456
setlocal varsofttabstop=
setlocal vartabstop=
setlocal virtualedit=
setlocal wincolor=
setlocal nowinfixheight
setlocal nowinfixwidth
setlocal wrap
setlocal wrapmargin=0
let s:l = 27 - ((12 * winheight(0) + 11) / 23)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 27
normal! 0
wincmd w
2wincmd w
exe 'vert 1resize ' . ((&columns * 97 + 97) / 195)
exe '2resize ' . ((&lines * 23 + 24) / 49)
exe 'vert 2resize ' . ((&columns * 97 + 97) / 195)
exe '3resize ' . ((&lines * 23 + 24) / 49)
exe 'vert 3resize ' . ((&columns * 97 + 97) / 195)
tabnext 1
badd +0 ~/cpp/vec.hpp
badd +0 storage.hpp
badd +0 main.cpp
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToOSI
let &winminheight = s:save_winminheight
let &winminwidth = s:save_winminwidth
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &g:so = s:so_save | let &g:siso = s:siso_save
nohlsearch
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
