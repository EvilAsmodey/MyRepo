package lt.vu.mif.jate.task01.bank;

import java.util.Locale;

public class Bank {
	
	
	String country = "";
	int code = 0;
	String iban = "";
	String bankName = "";
	String bankAdressPostCode = "";

	
	

	public Bank(String string, int i, String string2, String string3, String string4) {
		this.country = string;
		this.code = i;
		this.iban = string2;
		this.bankName = string3;
		this.bankAdressPostCode = string4;
	}

	public Locale getLocale(String string) {
		// TODO Auto-generated method stub
		return string;
	}

	public Object getCode() {
		// TODO Auto-generated method stub
		return null;
	}

	public String getBicCode() {
		// TODO Auto-generated method stub
		return null;
	}

	public String getName() {
		// TODO Auto-generated method stub
		return null;
	}

	public String getAddress() {
		// TODO Auto-generated method stub
		return null;
	}

}