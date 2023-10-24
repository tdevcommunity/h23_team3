"use client"
import { SessionProvider } from "next-auth/react";
import { ReactNode } from "react";
export const Authprovider: React.FC<{ children: ReactNode }> = ({ children }) => {
    return <SessionProvider>
        {children}
    </SessionProvider>
}