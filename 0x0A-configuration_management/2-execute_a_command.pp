# This manifest kills a process

exec {'pkill':
    command => '/usr/bin/pkill killmenow'
}
