## Echo server that uses unblocking sockets and OS events to manage the connections

Thanks to selectors we can let the OS manage our unblocking sockets
and keep us informed as soon as en event happens.
While receiving data from a client, an event won't
disappear until we read it completely, in some cases
it resolves a problem of receiving all the bytes
we're sent, despite of the size of the buffer.
