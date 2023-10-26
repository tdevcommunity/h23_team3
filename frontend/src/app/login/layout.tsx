import type { Metadata } from 'next'
import { Poppins } from 'next/font/google'
import '../globals.css'




export const metadata: Metadata = {
  title: 'Xmentor-login',
  description: 'se connecter',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="fr">
        
      <body>
     
          {children}
   
      </body>
    </html>
  )
}
