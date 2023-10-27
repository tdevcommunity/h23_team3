import type { Metadata } from 'next'
import { Poppins } from 'next/font/google'
import './globals.css'
import { Authprovider } from './Provider'
import Navbar from '@/components/ui/navbar'

const poppins = Poppins({
  weight: ['300', '400', '500', '600', '700', '800', '900'],
  subsets: ['latin']
})

export const metadata: Metadata = {
  title: 'Xmentor',
  description: 'Xmentor',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="fr">
      <body className={poppins.className}>
      <Navbar/>
        <Authprovider>
          {children}
        </Authprovider>
      </body>
    </html>
  )
}
