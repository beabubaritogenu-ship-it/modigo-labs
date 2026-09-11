def run_with_retries(results, max_attempts=3, on_failure="skip", log=None):
    # TODO: handle the mutable default argument problem correctly —
    # do not use a mutable object like [] directly as a default value.
    # Then simulate retrying through `results` according to the rules described.

    if log == None:
        log = []
    attempts = 0

    for outcome in results:
        if attempts >= max_attempts:
            break
        attempts +=1
        if outcome == "success":
            log.append("success")
            break

        elif outcome == "fail":
            if on_failure == "log":
                log.append("attempt failed")

            elif on_failure == "skip":
                continue


    return log