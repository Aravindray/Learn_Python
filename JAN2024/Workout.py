import re
import time
overallStart = time.time()

patternMail = re.compile(r'^[a-z0-9]+(((\.|\W)|\w)*[a-z0-9])*@[a-z]+(\.{1}[a-z]+)*(\.com)$')


validMailID = ['john.doe@example.com','jane_doe@example.com','jane-doe@example.com','jane+doe@example.com','jane.doe@subdomain.example.com','jane_doe@subdomain.example.com','jane-doe@subdomain.example.com','jane+doe@subdomain.example.com']

invalidMailID = ['john.doe@example','jane_doe@example..com','jane-doe@.example.com','jane+doe@examplecom','jane.doe@subdomain.example','jane_doe@subdomain.example..com','jane-doe@.subdomain.example.com','jane+doe@subdomain.examplecom']

for mailID in invalidMailID:
    start = time.time()
    result = patternMail.search(mailID)
    end = time.time()
    if result != None:
        print('Valid')
        print('execution time',end-start)
    else:
        print('NOT Valid')
        print('execution time',end-start)

overallEnd = time.time()

print('overall time',overallEnd-overallStart)