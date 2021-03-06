# mpaste

Lean, mean and clean, pastebinnin' machine.


## Dependencies

### Fedora/Korora

```bash
$ dnf install perl-Mojolicious perl-DBD-SQLite
```


## Quick Start

```bash
$ ./mpaste daemon
```

This will start up the pastebin server listening at `localhost` on port `3000`.


```bash
$ MPASTE_PASTE_DIR=/var/tmp/mpaste ./mpaste daemon --listen="http://*:5000"
```

Start the pastebin server listening globally on port `5000` and storing pastes in `/var/tmp/mpaste`.


## Environment Variables

The following environment variables allow you to modify the default behaviour of mpaste:

 - `MPASTE_HYPNOTOAD_LISTEN` - Set listen location for use with mojolicious hypnotoad. Multiple values can be delimited with a `,` or space. Defaults to `http://*:8000`.
 - `MPASTE_HOLD_TIME` - Set how long in seconds, a paste will stick around for. Defaults to `604800` (30 days).
 - `MPASTE_NO_HISTORY` - Set to hide paste history. Defaults to show available paste history.
 - `MPASTE_PASTE_DIR` - Set the directory where pastes and db are stored. Defaults to `/tmp/mpaste`.
 - `MPASTE_REAP_TIME` - Set the frequency, in seconds, to check for expired pastes. Defaults to `300` (5 minutes).
 - `MPASTE_SECRETS` - Set the secret passphrases used for signed cookies. Multiple values can be delimited with a `,` or space. Defaults to `mpaste` (ie. not very secure).
 - `MPASTE_UPLOAD_LIMIT` - Set the maximum upload limit in bytes. Defaults to `10485760` (10MB).

## License

[AGPLv3](http://www.gnu.org/licenses/agpl-3.0.en.html)
