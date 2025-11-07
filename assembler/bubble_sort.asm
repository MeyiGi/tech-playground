; Filename: bubble_sorted.nasm
; Assemble: nasm -felf64 bubble_sorted.nasm
; Link: ld -o bubble_sorted bubble_sorted.o
; Run: ./bubble_sorted

section .data
    array:  dd 5, 3, 4, 2, 6, 1        ; 32-bit signed ints
    len    equ 6

section .text
    global _start

_start:
    ; if len < 2, exit immediately
    mov     eax, len
    cmp     eax, 2
    jl      done

    ; outer_limit = len - 1
    mov     ecx, len
    dec     ecx              ; ecx = outer_limit (counts how many elements to bubble)

outer_loop:
    xor     r8d, r8d         ; r8d = swapped flag (0 = no swap yet)
    xor     esi, esi         ; index i = 0
    mov     edx, ecx         ; edx = inner_pass_count

inner_loop:
    ; load array[esi] into eax, array[esi+1] into ebx
    mov     eax, dword [array + rsi*4]
    mov     ebx, dword [array + rsi*4 + 4]

    cmp     eax, ebx
    jle     no_swap_here

    ; swap: store ebx into arr[esi] and eax into arr[esi+1]
    mov     dword [array + rsi*4], ebx
    mov     dword [array + rsi*4 + 4], eax

    mov     r8d, 1           ; swapped = 1

no_swap_here:
    inc     esi              ; index++
    dec     edx
    jnz     inner_loop

    ; if no swaps in this pass, array is sorted -> exit early
    cmp     r8d, 0
    je      done

    dec     ecx              ; outer limit--
    jnz     outer_loop

done:
    ; exit(0)
    mov     eax, 60          ; syscall: exit
    xor     edi, edi         ; status 0
    syscall