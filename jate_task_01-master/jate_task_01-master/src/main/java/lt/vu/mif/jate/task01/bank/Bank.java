package lt.vu.mif.jate.task01.bank;

import java.util.Locale;

public class Bank {
	
	private final String country;
	private final int code;
	private final String bic;
	private final String name;
	private final String adress;

	public Bank(String country, int code, String bic, String name, String adress) {
            this.country = country;
            this.code = code;
            this.bic = bic;
            this.name = name;
            this.adress = adress;
	}

        public Bank(String country, int code, String bic, String name) {
            this(country, code, bic, name, null);
        }

        public Bank(String country, int code, String bic) {
            this(country, code, bic, null);
        }

        public Bank(String country, int code) {
            this(country, code, null);
    }
        
	public Locale getLocale() {
            return new Locale("en", this.country);
	}

	public Integer getCode() {
            return this.code;
	}

	public String getBicCode() {
            return this.bic;
	}

	public String getName() {
            return this.name;
	}

	public String getAddress() {
            return this.adress;
	}

}