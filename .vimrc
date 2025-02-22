" .vimrc * version 2.3.4-u0.1

set nocp               "nocompatible

syntax on
filetype plugin indent on

".vimrc2
if filereadable(glob("~/.vimrc2"))
    so ~/.vimrc2
endif

"-------------------- ПЛАГИНЫ --------------------

"netrw
let g:netrw_banner = 0
let g:netrw_preview = 1
let g:netrw_browse_split = 2


"-------------------- ОПЦИИ --------------------

set sh=/bin/bash        "оболочка для запуска внешних команд
set shellcmdflag=-c
"if &diff == 'nodiff'
"    set shellcmdflag=-ci    "интерактивный shell (включение .bashrc)
"endif

"if filereadable(glob("~/bin/bash-aliases"))
"    set sh=~/bin/bash-aliases
"    set shellcmdflag=-c
"endif

set foldmethod=marker
set foldmarker=//->,//<-

set enc=utf-8           "кодировка
"set ff=unix            "'fileformat' - символ конца строки при чтении/записи в файл
set mouse=a             "включение мыши
set ai                  "'autoindent' - сохранение табуляции при переходе на новую строку
set smartindent         "автоматическая табуляция внутри блоков
set nu                  "'number' - нумерация строк 
set shiftwidth=4        "размер отступа
"set tabstop=8          "размер табуляции
set softtabstop=4       "вставка/удаление отступов как табуляций 
set smarttab            "вставлять по TAB отступ размером shiftwidth в начале строки	
set expandtab           "заменять табуляции пробелами
set scrolloff=2         "количество строк до края при скроллинге
set wrap                "переносить длинные строки при отображении
set magic               "магия в регулярных выражениях
set shortmess+=I        "без всплывающего экрана
set tm=1000 ttm=100     "быстрый Esc ('timeoutlen', 'ttimeoutlen')
set sc                  "'showcmd' - показывать команду при вводе
set aw                  "'autowrite' - записывать изменения при смене файла
set ls=1                "'laststatus' - показывать строку состояния
set is                  "'incsearch' - инкрементная подсветка поиска
set nohls               "'hlsearch' - подсветка результатов поиска
set ssop-=curdir ssop+=sesdir   "'sessionoptions', относительные имена файлов
set novb                "'visualbell' - визуальный звуковой сигнал
set wildmenu            "меню автодополнения в командной строке 
set path+=/usr/include/x86_64-linux-gnu,/usr/include/c++/11     "поиск заголовочных файлов
set spr                 "'splitright' - новое окно справа
set bs=indent,eol,start     "'backspace' - свободное удаление по BS
set ul=1000             "'undolevels' - размер истории изменений
"set kp=man              "'keywordprg' - программа просмотра ключевых слов
"set km=startsel,stopsel    "'keymodel' - выделение стрелками
"set bo=all             "'belloff' - отключение звукового сигнала

set fdc=1               "'foldcolumn' - столбец индикации складок
set sm                 "'showmatch' - подсветка парных скобок

"'statusline' - строка состояния
set stl=%t\ %<[%{expand('%:p:~:h')}]%(\ %h%m%r%)%(\ %k%)\ \ w%{winnr()}\ b%{winbufnr(0)}\ %=%b\ 0x%B\ \ %-12.(%l,%c%V%)\ %P        

set penc=cp1251         "кодировка принтера
set popt=left:5pc       "левое поле при печати
"set popt=paper:A5      "размер бумаги
"set popt+=portrait:n   "альбомная ориентация
"set popt+=header:0     "без заголовка
set pfn=courier:h8      "шрифт 8пт при печати

if &term =~ "linux"
    set bg=dark
"    set bg=light
else
    set bg=dark             "шрифты, оптимальные для тёмного фона
endif

set hl+=M:Type          "подсветка индикатора режима
set t_Co=8              "количество цветов
"set hls                "подсветка результатов последнего поиска
"set cul                "подсветка текущей строки
"set cuc                "подсветка текущего столбца

"set tw=80              "'textwidth' - длина строки до переноса при вводе
"set wm=50              "'wrapmargin' - отступ от правого края до переноса при вводе
"set ls=2               "всегда показывать строку состояния
"set list               "показывать непечатаемые символы
"set sb                 "'splitbelow' - открывать новое окно ниже текущего
"set noea                 "'equalalways' - всегда выравнивать размеры окон приоткрытии нового
"set ve=block           "'virtualedit' - выход за конец строки (при блочном выделении)
"set ws                 "'wrapscan' - поиск переходит через конец файла

"set ft=sh              "shell color scheme
"set spell              "включить проверку правописания


"-------------------- РУСИФИКАЦИЯ --------------------

set keymap=russian-jcukenwin
set iminsert=0
set imsearch=0
set spelllang=ru_yo,en_us

set langmap=ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ;`qwertyuiop[]asdfghjkl\\;'zxcvbnm\\,.~QWERTYUIOP{}ASDFGHJKL:\\"ZXCVBNM<>

noremap! <C-L> <C-^>
lnoremap <C-L> <C-^>
cnoremap <C-S> <C-L>
"inoremap <C-B> <C-L>


"-------------------- КУРСОР --------------------

highlight Cursor guifg=NONE guibg=SeaGreen
highlight lCursor guifg=NONE guibg=DarkCyan

"Форма курсора
if &term =~ "xterm"
    let &t_SI = "\e[5 q"
    let &t_EI = "\e[3 q"
    let &t_SR = "\e[1 q"
endif


"-------------------- ГОРЯЧИЕ КЛАВИШИ --------------------

"TERM WINDOW
"terminal normal mode
tmap <F2> <C-W>N

"bash terminal
nmap <silent> <leader>t <esc>:call term_start("bash",
            \{"term_name": "bash", "term_finish": "close"})<cr>

"python terminal
nmap <silent> <leader>T <esc>:call term_start("bash -c py",
            \{"term_name": "python", "term_finish": "close"})<cr>


"----------------------------------------

"сохранение сессии
nmap <F1> :mks!<cr>
vmap <F1> <esc><F1><cr>
imap <F1> <esc><F1><cr>

"сохранение
map <F2> <esc>:up<cr>
map! <F2> <esc>:up<cr>

"ctags
set <S-F2>=[1;2Q
nnoremap <S-F2> <esc>:!make ctags<cr>
vmap <S-F2> <esc><S-F2><cr>
imap <S-F2> <esc><S-F2><cr>

"make
nnoremap <F3> <esc>:!make<cr>
imap <F3> <esc><F3>
vmap <F3> <esc><F3>

"GDB
set <S-F3>=[1;2R
nnoremap <S-F3> <esc>:!make debug<cr>
imap <S-F3> <esc><S-F3>
vmap <S-F3> <esc><S-F3>

"make TARGET
set <F17>=[1;5R   "C-F3
nnoremap <F17> <esc>:!make TARGET="%:t:r"<cr>
imap <F17> <esc><F17>
vmap <F17> <esc><F17>

"make from file dir
nnoremap <leader><F3> <esc>:!cd "%:p:h" && make<cr>

"редактировать .vimrc
com! VimrcEdit new ~/.vimrc
nmap <F4> :VimrcEdit<cr>
imap <F4> <esc><F4><cr>

"редактировать .vimrc2
com! VimrcEdit2 new ~/.vimrc2
set <S-F4>=[1;2S
nmap <S-F4> :VimrcEdit2<cr>
imap <S-F4> <esc><S-F4><cr>

"перезагрузить .vimrc
"nmap <F5> :so ~/.vimrc <bar> redraw <bar> echom ".vimrc reloaded"<cr>	
com! VimrcReload so ~/.vimrc | redraw | echom ".vimrc reloaded"
map <silent> <F5> <esc>:VimrcReload<cr>
map! <F5> <esc><F5>

"выход
nmap <F6> :q<cr>
vmap <F6> <esc>:q<cr>
imap <F6> <esc>:q<cr>

nmap <S-F6> :q!<cr>
vmap <S-F6> <esc>:q!<cr>
imap <S-F6> <esc>:q!<cr>

"переключатель подсветки синтаксиса
nnoremap <silent> <F7> :call SynSwitch()<cr>
vmap <F7> <esc><F7>
imap <F7> <esc><F7>

fu! SynSwitch()
    if exists("b:current_syntax")
        syntax off
        echo "syntax off"
    else
        syntax on
        echo "syntax on"
    endif
endfu

"vimgrep
nnoremap <S-F7> <esc>:G <C-R><C-W><cr>
vmap <S-F7> <esc><S-F7>
imap <S-F7> <esc><S-F7>

"переключатель нумерации
nmap <F8> :set nu!<cr>
nmap <S-F8> :set rnu!<cr>

"quickfix
nmap <F9> :copen<cr>
imap <F9> <esc><F9><cr>
vmap <F9> <esc><F9><cr>

"закрыть quickfix
nmap <S-F9> :cclose<cr>	
imap <S-F9> <esc><S-F9>
vmap <S-F9> <esc><S-F9>

"следующая строка quickfix
nmap <F10> :cnext<cr>	
imap <F10> <esc><F10>
vmap <F10> <esc><F10>

"предыдущая строка quickfix
nmap <S-F10> :cprev<cr>	
imap <S-F10> <esc><S-F10>
vmap <S-F10> <esc><S-F10>

"запуск программы
fu! Ft() 
    silent! up
    if &ft == 'c'
        !gc "%:p:r"
        "!gcc -o "%:r" "%" -lm -time && "%:p:r" 
    elseif &ft == 'cpp'
        !g++ -std=c++17 -g3 -o "%:r" "%" && "%:p:r"
    elseif &ft == 'pascal'
        !fpc "%" 2> >(sed '/ld.bfd/d') && "%:p:r" 
    elseif &ft == 'python'
        !py "%"
    elseif &ft == 'sh'
        !bash "%"
    elseif &ft == 'asm'
        !as -o "%:r".o "%" && ld -o "%:r" "%:r".o && "%:p:r"
    elseif &ft == 'php'
        !php "%"
    elseif &ft == 'javascript'
        !node "%"
    elseif &ft == 'java'
        !(javac % && java -ea %:r)
    elseif &ft == 'plaintex'
        !tex "%" && evince "%:p:r.dvi"
    elseif &ft == 'tex'
        !pdflatex "%" && evince "%:p:r.pdf"
    endif
endfu

fu! Ft2() 
    silent! up
    if &ft == 'c'
        !gc "%:p:r"
        "!gcc -o "%:r" "%" -lm -time && "%:p:r" 
    elseif &ft == 'cpp'
        !g++ -Wfatal-errors -o "%:r" "%" && "%:p:r"
    elseif &ft == 'pascal'
        !fpc "%" 2> >(sed '/ld.bfd/d') && "%:p:r" 
    elseif &ft == 'python'
        !py -i "%"
    elseif &ft == 'sh'
        !bash "%"
    elseif &ft == 'asm'
        !gcc -no-pie -s -o "%:r" "%" && "%:p:r"
    elseif &ft == 'php'
        !php "%"
    elseif &ft == 'javascript'
        !node "%"
    elseif &ft == 'java'
        !(javac % && java -ea %:r)
    elseif &ft == 'plaintex'
        !tex "%" && evince "%:p:r.dvi"
    elseif &ft == 'tex'
        !pdflatex "%" && evince "%:p:r.pdf"
    endif
endfu

nnoremap <S-F11> <esc>:call Ft()<cr>
imap <S-F11> <esc><S-F11>

nmap <M-Down> <S-F11>
imap <M-Down> <S-F11>
nmap zx <S-F11>

nmap <M-Up> <esc>:call Ft2()<cr>
imap <M-Up> <esc><M-Up>
nmap zX <M-Up>

"асинхронный запуск программы
fu! Fta() 
    silent! up
    if &ft == 'c'
        let cmd = 'gc "%:p:r"'
        "ter ++shell gcc -o "%:r" "%" -lm -time && "%:p:r" 
    elseif &ft == 'cpp'
        let cmd = 'g++ -o "%:r" "%" && "%:p:r"'
    elseif &ft == 'pascal'
        let cmd = 'fpc "%" 2> >(sed ''/ld.bfd/d'') && "%:p:r"'
    elseif &ft == 'python'
        if expand("%:e:e") == 'vim.py'
            py3file %
            return
        else
            let cmd = 'py "%"'
        endif
    elseif &ft == 'sh'
        let cmd = 'bash "%"'
    elseif &ft == 'asm'
        let cmd = 'as -o "%:r".o "%" && ld -o "%:r" "%:r".o && "%:p:r"'
    elseif &ft == 'php'
        let cmd = 'php "%"'
    elseif &ft == 'javascript'
        let cmd = 'node "%"'
    elseif &ft == 'java'
        let cmd = '(javac % && java -ea %:r)'
    elseif &ft == 'plaintex'
        let cmd = 'tex "%" && evince "%:p:r.dvi"'
    elseif &ft == 'tex'
        let cmd = 'pdflatex "%" && evince "%:p:r.pdf"'
    else
        return
    endif

    exe "ter ++shell" cmd
endfu

fu! Ft2a() 
    silent! up
    if &ft == 'c'
        let cmd = 'gc "%:p:r"'
        "ter ++shell gcc -o "%:r" "%" -lm -time && "%:p:r" 
    elseif &ft == 'cpp'
        let cmd = 'g++ -Wfatal-errors -o "%:r" "%" && "%:p:r"'
    elseif &ft == 'pascal'
        let cmd = 'fpc "%" 2> >(sed ''/ld.bfd/d'') && "%:p:r"'
    elseif &ft == 'python'
        if expand("%:e:e") == 'vim.py'
            py3file %
            return
        else
            let cmd = 'py -i "%"'
        endif
    elseif &ft == 'sh'
        let cmd = 'bash "%"'
    elseif &ft == 'asm'
        let cmd = 'gcc -no-pie -s -o "%:r" "%" && "%:p:r"'
    elseif &ft == 'php'
        let cmd = 'php "%"'
    elseif &ft == 'javascript'
        let cmd = 'node "%"'
    elseif &ft == 'java'
        let cmd = '(javac % && java -ea %:r)'
    elseif &ft == 'plaintex'
        let cmd = 'tex "%" && evince "%:p:r.dvi"'
    elseif &ft == 'tex'
        let cmd = 'pdflatex "%" && evince "%:p:r.pdf"'
    else
        return
    endif

    exe "ter ++shell" cmd
endfu

nmap <silent> <leader><Down> <esc>:call Fta()<cr>
nmap <leader>x <leader><Down>

nmap <silent> <leader><Up> <esc>:call Ft2a()<cr>
nmap <leader>X <leader><Up>

"запуск последней внешней команды
nnoremap <S-F12> <esc>:up<cr>:!!<cr>

"переключатель видимости специальных символов
set <F16>=[19;5~  "<C-F8>
nmap <F16> :set list!<cr>

"Compile and run gdb       
nnoremap <S-M-Down> <esc>:!gcd "%:p:r"<cr>
imap <S-M-Down> <esc><S-M-Down>

"вставка с заменой
nnoremap <leader>S dd"0P

"удаление в обход регистров
nnoremap <leader>d "_dd
vnoremap <leader>d "_d

"разрыв строки
nnoremap <leader>J i<cr><esc>

"вставка по пробелу
nnoremap <leader><Space> i‗<esc>r

"переход по номеру байта
nnoremap gb go

"вставка новой строки
nnoremap go o<esc>
nnoremap gO O<esc>
nnoremap <leader>o o<esc>
nnoremap <leader>O O<esc>

"вставка скопированного
nnoremap <leader>p "0p
nnoremap <leader>P "0P

"сдвиг и копирование строк
"nmap <silent> <C-j> :silent! m.+1<cr>
"nmap <silent> <C-Down> :silent! m.+1<cr>
vmap <silent> <C-j> :m<Home>silent! <End>'>+1<cr>gv
vmap <silent> <C-Down> :m<Home>silent! <End>'>+1<cr>gv

fu! Modif_test()
    if !&modifiable
        echoh ErrorMsg | echo "Not modifiable!" | echoh None
        return 0
    else
        return 1
    endif
endfu

nmap <silent> <C-j> :<C-U>call Move_down()<cr>
nmap <silent> <C-Down> :<C-U>call Move_down()<cr>

fu! Move_down() range
    if !Modif_test() | return | endif

    let c = col(".")
    let l0 = line(".")
    let l1 = min([l0 + v:count1 - 1, line("$")])

    silent! exe l0 "," l1 "m" (l1 + 1)

    let l0_ = l1 < line("$") ? l0 + 1 : l0
    call cursor(l0_, c)
endfu

"nmap <silent> <C-k> :silent! m.-2<cr>
"nmap <silent> <C-Up> :silent! m.-2<cr>
vmap <silent> <C-k> :m<Home>silent! <End>'<-2<cr>gv
vmap <silent> <C-Up> :m<Home>silent! <End>'<-2<cr>gv

nmap <silent> <C-k> :<C-U>call Move_up()<cr>
nmap <silent> <C-Up> :<C-U>call Move_up()<cr>

fu! Move_up() range
    if !Modif_test() | return | endif

    let c = col(".")
    let l0 = line(".")
    let l1 = min([l0 + v:count1 - 1, line("$")])

    silent! exe l0 "," l1 "m" (l0 - 2)

    call cursor(max([l0 - 1, 1]), c)
endfu

nmap <silent> <leader>j :co.<cr>
nmap <silent> <leader>k :co.-1<cr>

"nmap <C-Right> >>
"nmap <C-Left> <<
"nmap <leader>. >>
"nmap <leader>, <<

vmap <C-Right> >gv
vmap <C-Left> <gv
vmap <leader>. >gv
vmap <leader>, <gv

nmap <silent> gl :<C-U>call Move_hor(1)<cr>
nmap <silent> gh :<C-U>call Move_hor(-1)<cr>

nmap <silent> <C-Right> :<C-U>call Move_hor(1)<cr>
nmap <silent> <C-Left> :<C-U>call Move_hor(-1)<cr>

fu! Move_hor(dir) range
    if !Modif_test() | return | endif

    let c = col(".")
    let l0 = line(".")
    let l1 = min([l0 + v:count1 - 1, line("$")])

    exe "normal ^"
    let ci0 = col(".")

    if a:dir > 0
        exe l0 "," l1 ">"
    else
        exe l0 "," l1 "<"
    endif

    call cursor(l0, 0)
    exe "normal ^"
    let ci1 = col(".")
    call cursor(0, ci1 + c - ci0)
endfu

"escape nowait
"nmap <nowait>  
"vmap <nowait>  

"изменение регистра слова
nnoremap <leader>u g~iWW

"выход в нормальный режим
"inoremap jk <esc>

"переключатель подсветки столбца и строки
noremap <leader>c <esc>:set cuc!<cr>
noremap <leader>l <esc>:set cul!<cr>

"virtual edit
fu! Ve() 
    if &ve == ''
        let &ve = 'all'
    else
        let &ve = ''
    endif
    set ve?
endfu
noremap <leader>v <esc>:call Ve()<cr>
"<C-S-F8>
set <F15>=[19;6~
nmap <F15> <leader>v

"строка состояния (last status)
fu! Ls() 
    if &ls == 1
        let &ls = 2
    elseif &ls == 2
        let &ls = 1
    endif
    set ls?
endfu
noremap <leader>s <esc>:call Ls()<cr>

"инкремент версии
fu! VerInc()
    if empty(expand('%:e'))
        echoh ErrorMsg | echo "No extension!" | echoh None
        return
    endif

    let m = matchlist(@%, '\vv(\d+)\.')

    if empty(m)
        let filename = expand('%:r')..'v2.'..expand('%:e') 
    else
        let n = m[1] + 1
        let filename = substitute(@%, '\vv(\d+)\.', 'v'..n..'.', '')
    endif

    if !empty(glob(filename))
        echoh ErrorMsg | echo "File "..filename.." already exists!" | echoh None
    else
        exe 'save' filename
    endif
endfu
nnoremap <leader>n <esc>:call VerInc()<cr>

"заковычиватель
nnoremap <leader>q ciW""PW

"расковычиватель
nnoremap <leader>w di"hPlxxW

"комментировать/раскомментировать 
nnoremap <leader>z 0i#j0
nnoremap <leader>Z 0xj0

"комментировать\раскомментировать
nnoremap <leader>[ <esc>gI//<esc>:s+////++e<cr>+
"imap <leader>[ <esc><leader>[

fu! Comment() 
    if &ft == 'c' || &ft == 'cpp' || &ft == 'pascal' || &ft == 'java'
        let comstr = '//'
    elseif &ft == 'sh' || &ft == 'python'
        let comstr = '#'
    elseif &ft == 'vim'
        let comstr = '"'
    elseif &ft == 'tex' || &ft == 'plaintex'
        let comstr = '%'
    else
        let comstr = '#'
    endif

    exe "normal 0i"..comstr.."\<esc>"
    exe 's+^'..comstr..'\(\s*\)'..comstr..'+\1+e'
    normal +
endfu

noremap <C-_> :call Comment()<cr>
ounmap <C-_>
imap <C-_> <esc><C-_>

map <leader>] <C-_>
ounmap <leader>]
"imap <leader>] <esc><leader>]

map z/ <C-_>
ounmap z/

"TODO
nnoremap <leader><leader>t i#TODOj

"cursor position
noremap <leader><leader>c :echo getcurpos()<cr>

"выход в нормальный режим
"inoremap jk <esc>


"-------------------- КОМАНДЫ --------------------

com! Test exe "norm 3wd2l\<esc>" | w	"тест пользовательской команды

com! -nargs=1 -complete=file -bar L topleft vsp <args>                  "новая вкладка слева
com! -nargs=1 -complete=file -bar R botright vsp <args>                 "новая вкладка справа
com! -nargs=1 -complete=file -bar U topleft sp <args>                   "новая вкладка сверху
com! -nargs=1 -complete=file -bar D botright sp <args>                  "новая вкладка снизу
com! -nargs=1 -complete=file -bar H sp <args> | resize 12 | winc j      "открытие файла над текущим
com! -nargs=1 -complete=file -bar T $tabnew <args>.c | H <args>.h            "открытие модуля С
com! -nargs=1 -complete=file TR R <args>.c | H <args>.h                 "открытие модуля С справа
com! -nargs=1 -complete=file TL L <args>.c | H <args>.h                 "открытие модуля С слева
com! -nargs=1 -complete=file TT 
            \T <args> |
            \0r template.c |
            \%s/__basename__/<args>/g |
            \winc k |
            \0r template.h |
            \%s/__BASENAME__/\U<args>/g |
            \%s/__startedit__// |
            \startinsert

com! -bang C tabclose<bang>               "закрытие вкладки
com! CL winc t | q | q | winc p           "закрытие модуля слева
com! CR winc b | q | q | winc p           "закрытие модуля справа
com! CM winc k | q | q                    "закрытие текущего модуля

com! -nargs=? -complete=tag G vimgrep/<args>/gj **/*.[ch] | copen       "vimgrep + quickfix
com! -nargs=1 S %s/<args>/gc                                            "global substitute


"-------------------- ПОДСВЕТКА СИНТАКСИСА --------------------

"выделение текста перед тире
match Type /^.\{-}—\@=/

"весь текст жирным
"highlight MyGroup cterm=bold
"match MyGroup /./


"-------------------- АВТОКОМАНДЫ --------------------

augroup main
    au!

    "Напоминание о перезагрузке bash_aliases      
    "au BufWritePost .bash_aliases echo "Re-source .bashrc!"

    "Перезагрузка .vimrc
    au BufWritePost ~/.vimrc,~/.vimrc2 VimrcReload  

    "Переход на позицию последнего редактирования
    au BufRead ~/.bash_aliases,~/.vimrc silent! normal! g`.
    au BufRead ~/.bash_aliases2,~/.vimrc2 silent! normal! g`.

    "Переключение цветовой схемы
    "au BufEnter * colo default
    "au BufEnter *.c colo ron

    "Распознавание типа файла
    au BufNewFile,BufRead .vundlerc set ft=vim
    au BufNewFile,BufRead *.inc set ft=c

    "Обновление экрана
    "au BufWinEnter * redraw
    "au BufWinLeave * redraw
augroup end

augroup ab
    au!

    au FileType c,cpp   call Ab_c() 
    au FileType cpp     call Ab_cpp() 
    au FileType python  call Ab_py() 
    au FileType java    call Ab_java()
augroup end

augroup map
    au!

    au FileType c,cpp   call Map_c() 
    au FileType cpp     call Map_cpp() 
augroup end


"--------------- ГОРЯЧИЕ КЛАВИШИ (спец.) --------------

"c
fu! Map_c()
    "{} block
    nnoremap <buffer> <leader>} :s/\(\S\)\s*$/\1 /e<cr>A <bs>{<cr> <bs><cr>}<esc>kI
    nmap <buffer> <leader>{ <leader>}
    nmap <buffer> <leader>b <leader>}

endfu

"cpp
fu! Map_cpp()
    "cout/cin
    nnoremap <buffer> <leader>< Icout << <esc>$a << endl;<esc>$
    nnoremap <buffer> <leader>> Icin >> <esc>$a;<esc>$

endfu


"-------------------- АББРЕВИАТУРЫ --------------------

"c
fu! Ab_c()
    iab <buffer> #i #include <stdio.h><cr><cr>int main() {<cr>}<esc>O
    iab <buffer> #h #include <stdio.h><cr>#include <stdlib.h>
    iab <buffer> #l #include <stdlib.h>
    iab <buffer> #m #include <math.h>

    iab <buffer> pr  printf("");<left><left><left>
    iab <buffer> prn printf("\n");<esc>F\i
    iab <buffer> pri printf("%d\n", _);<esc>F_s
    iab <buffer> prl printf("%ld\n", _);<esc>F_s
    iab <buffer> prx printf("%x\n", _);<esc>F_s
    iab <buffer> prc printf("%c\n", _);<esc>F_s
    iab <buffer> prs printf("%s\n", _);<esc>F_s
    iab <buffer> prf printf("%f\n", _);<esc>F_s
    iab <buffer> prfg printf("%g\n", _);<esc>F_s
    iab <buffer> prfe printf("%e\n", _);<esc>F_s
    iab <buffer> prp printf("%p\n", _);<esc>F_s
    iab <buffer> prF printf("\n");<cr>fflush(stdout);<esc>kF\i

    iab <buffer> fori for(int i = 0; i < _; i++) <esc>F_s
    iab <buffer> forj for(int j = 0; j < _; j++) <esc>F_s
    iab <buffer> fork for(int k = 0; k < _; k++) <esc>F_s
    iab <buffer> iff if() {<cr><cr>}<esc>2k$F)i
    iab <buffer> ifel if() {<cr><cr>} else {<cr><cr>}<esc>4k$F)i

    iab <buffer> }} {<cr> <bs><cr>}<esc>kI
    iab <buffer> {{ {<cr> <bs><cr>}<esc>kI
    iab <buffer> fv void f() {<cr><cr>}<esc>2k$F)i
    iab <buffer> fi int f() {<cr><cr>}<esc>2k$F)i
    iab <buffer> fl long f() {<cr><cr>}<esc>2k$F)i
    iab <buffer> fc char f() {<cr><cr>}<esc>2k$F)i
endfu

"cpp
fu! Ab_cpp()
    iab <buffer> #I #include <iostream><cr><cr>using namespace std;<cr><cr>int main() {<cr>}<esc>O

    iab <buffer> co cout << x;<esc>Fxs
    iab <buffer> cod cout << x << ' ';<esc>Fxs
    iab <buffer> coe cout << x << endl;<esc>Fxs
    iab <buffer> ci cin >> x;<esc>Fxs
endfu    

"python
fu! Ab_py()
    iab <buffer> pr print()<esc>i

    iab <buffer> fori for i in range():<esc>F)i
    iab <buffer> forj for j in range():<esc>F)i
    iab <buffer> fork for k in range():<esc>F)i
endfu

"java
fu! Ab_java()
    iab <buffer> sop System.out.println();<esc>F)i
    iab <buffer> sopp System.out.print();<esc>F)i
endfu

"global
iab #b #!/usr/bin/bash
iab #p #!/usr/bin/python3

iab --- —
